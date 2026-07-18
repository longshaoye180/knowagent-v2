import os

from agents import Agent

from context.app_context import AppContext


def create_summary_agent() -> Agent[AppContext]:

    return Agent(
            name = "Summary Agent",
            instructions="""
你负责总结历史会话。

要求：

1. 保留长期目标
2. 保留重要上下文
3. 保留未完成任务
4. 删除闲聊
5. 输出不要超过300字
""",
            model=os.getenv("LLM_MODEL")
        )