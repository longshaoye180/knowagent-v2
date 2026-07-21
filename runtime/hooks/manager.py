from typing import List

from runtime.hooks.base import BaseHook


class HookManager:

    def __init__(self, hooks: List[BaseHook]):
        self.hooks = hooks or []


    async def on_request_start(self, context):

        for hook in self.hooks:
            await hook.on_request_start(context)

    async def on_request_end(self, context):
        for hook in self.hooks:
            await hook.on_request_end(context)

    async def on_tool_start(self, tool_name, context):
        for hook in self.hooks:
            await hook.on_tool_start(tool_name, context)

    async def on_tool_end(self, tool_name, output, context):
        for hook in self.hooks:
            await hook.on_tool_end(tool_name, output, context)

    async def on_agent_start(self, agent, context):
        for hook in self.hooks:
            await hook.on_agent_start(agent, context)

    async def on_agent_end(self, agent, context):
        for hook in self.hooks:
            await hook.on_agent_end(agent, context)