import os

from agents import Agent

from context.app_context import AppContext


def create_planner_agent() -> Agent[AppContext]:

    return Agent(
        name="Planner",
        model=os.getenv("LLM_MODEL"),
        instructions="""
你是一名企业 AI Planner。

你的职责：

1. 理解用户目标。

2. 判断需要哪些 Agent。

例如：

天气

→ Weather Agent

数学

→ Math Agent

聊天

→ Assistant

不要直接回答问题。

只负责制定计划。       
"""
    )