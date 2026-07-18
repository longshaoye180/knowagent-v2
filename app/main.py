import asyncio
import os

from agents import set_default_openai_client, set_tracing_disabled, Runner, set_default_openai_api, \
    SQLiteSession
from dotenv import load_dotenv
from openai import AsyncOpenAI
from openai.types.responses import ResponseTextDeltaEvent

from agent.assistant import create_assistant
from agent.math_agent import create_math_agent
from agent.planner_agent import create_planner_agent
from agent.reflection_agent import create_reflection_agent
from agent.summary_agent import create_summary_agent
from agent.weather_agent import create_weather_agent
from context.app_context import AppContext
from memory.memory_store import MemoryStore
from runtime.logger import RuntimeLogger
from service.reflection_service import ReflectionService
from service.summary_service import SummaryService
from tools.calculator import calculate
from tools.preference import remember_preferences
from tools.profile import remember_profile
from tools.registry import ToolRegistry
from tools.remember_memory import remember_memory
from tools.weather import get_weather

load_dotenv()

async def main():

    client = AsyncOpenAI(
        api_key=os.getenv("LLM_API_KEY"),
        base_url=os.getenv("LLM_BASE_URL"),
    )

    set_default_openai_client(client)

    set_default_openai_api("chat_completions")

    set_tracing_disabled(True)

    registry = ToolRegistry()

    registry.register("weather", get_weather )

    registry.register("calculator", calculate)

    registry.register("remember_profile", remember_profile)

    registry.register("remember_preference", remember_preferences)

    registry.register("remember_memory", remember_memory)

    #Runtime Agents
    summary_agent = create_summary_agent()

    reflection_agent = create_reflection_agent()

    planner_agent = create_planner_agent()

    #Business Agents
    weather_agent = create_weather_agent(registry)

    math_agent = create_math_agent(registry)

    assistant = create_assistant(
        registry,
        weather_agent,
        math_agent,
    )

    session = SQLiteSession(
        "demo-session",
    )

    memory = MemoryStore()
    app_context = AppContext(
        memory=memory,
    )

    while True:
        user_input = input("\nUser> ")
        if user_input.lower() == "exit":
            break

        app_context.current_query = user_input

        result = Runner.run_streamed(
            starting_agent=assistant,
            input=user_input,
            session=session,
            context=app_context,
        )

        print()

        async for event in result.stream_events():
            if (
                event.type == "raw_response_event"
                and isinstance(event.data, ResponseTextDeltaEvent)
            ):
                print(event.data.delta, end="", flush=True)

            elif event.type == "agent_updated_stream_event":
                RuntimeLogger.title("Agent Switch")
                RuntimeLogger.info(f"{event.new_agent.name}")

            elif ( event.type == "run_item_stream_event" and event.name == "tool_called"):
                RuntimeLogger.title("Tool Called")
                RuntimeLogger.info(f"{event.item.raw_item.name}")


            elif ( event.type == "run_item_stream_event" and event.name == "tool_output"):
                RuntimeLogger.title("Tool Output")
                RuntimeLogger.info(f"{event.item.output}")


        print("\n")

        print("=" * 60)
        print(f"Last Agent : {result.last_agent.name}")

        print()
        print(result.final_output)
        print()

        if(hasattr(result.final_output, "model_dump")):
            RuntimeLogger.info(
                str(result.final_output.model_dump())
            )

        print("=" * 60)

        RuntimeLogger.title("Memory")
        RuntimeLogger.info(str(app_context.memory.all()))

        RuntimeLogger.title("Generate History")

        await SummaryService.maybe_generate_summary(
            app_context,
            session,
            summary_agent
        )

        await ReflectionService.reflect(
            context=app_context,
            session=session,
            reflection_agent=reflection_agent,
        )


if __name__ == "__main__":
    asyncio.run(main())


