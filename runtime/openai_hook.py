from agents import RunHooks
from runtime.logger import RuntimeLogger


class LoggingRunHooks(RunHooks):

    async def on_agent_start(self, context, agent):

        RuntimeLogger.title("Agent Start")

        RuntimeLogger.info(f"Agent: {agent.name}")


    async def on_agent_end(
        self,
        context,
        agent,
        output,
    ):
        RuntimeLogger.info("Agent End")