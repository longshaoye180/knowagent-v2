import os

from agents import Agent

from context.app_context import AppContext
from tools.registry import ToolRegistry


def create_math_agent(
        registry: ToolRegistry,
) -> Agent[AppContext]:
    """
    数学专家
    """

    return Agent(
        name="Math Agent",
        handoff_description="""
负责数学计算。

包括：

- 加减乘除
- 百分比
- 平方
- 开方
""",
        instructions="""
你是一位数学计算专家。

所有数学计算

必须调用 calculate 工具。

不要自己心算。

不要直接计算。

任何数学表达式都调用 Tool。
""",
        model=os.getenv("LLM_MODEL"),
        tools=registry.get_tools(
            ["calculator"]
        )
    )