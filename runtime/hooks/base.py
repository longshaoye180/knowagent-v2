from typing import Any


class BaseHook:

    async def on_request_start(self, context: Any):
        pass

    async def on_request_end(self, context: Any):
        pass

    async def on_agent_start(self, agent, context: Any):
        pass

    async def on_agent_end(self, agent, context: Any):
        pass

    async def on_tool_start(self, tool_name: str, context: Any):
        pass

    async def on_tool_end(self, tool_name: str, output, context: Any):
        pass
