from agents import function_tool, RunContextWrapper

from context.app_context import AppContext
from service.memory_service import MemoryService


@function_tool
def remember_memory(
        ctx: RunContextWrapper[AppContext],
        content: str
) -> str:

    MemoryService.remember(
        context=ctx.context,
        content=content,
    )

    return "长期记忆保存成功。"