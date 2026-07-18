from agents import Runner, SQLiteSession

from context.app_context import AppContext
from service.memory_service import MemoryService


class ReflectionService:

    @classmethod
    async def reflect(
            cls,
            context: AppContext,
            session: SQLiteSession,
            reflection_agent,
    ):

        items = await session.get_items()

        if not items:
            return

        history = "\n".join(
            str(item)
            for item in items[-20:]
        )

        result = await Runner.run(
            reflection_agent,
            history,
            context=context,
        )

        output = result.final_output.strip()

        if output.upper() == "NONE":
            return

        for line in output.splitlines():

            content = line.strip()

            if not content:
                continue

            MemoryService.remember(
                context,
                content,
            )