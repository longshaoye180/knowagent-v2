from agents import RunHooks


class OpenAIRunHooksAdapter(RunHooks):

    def __init__(self, hook_manager,):
        self.hook_manager = hook_manager

    async def on_agent_start(self, context, agent):
        await self.hook_manager.on_agent_start(agent, context)

    async def on_agent_end(
        self,
        context,
        agent,
        output,
    ):
        await self.hook_manager.on_agent_end(agent, context)