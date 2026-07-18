import os

from agents import Agent

from context.app_context import AppContext


def create_reflection_agent() -> Agent[AppContext]:

    return Agent(
        name='Reflection Agent',
        model=os.getenv("LLM_MODEL"),
        instructions="""
你负责分析最近一次对话。

请判断：

哪些信息值得保存为长期记忆。

例如：

- 长期目标
- 长期计划
- 长期兴趣
- 长期技能
- 长期身份变化

不要保存：

- 问候语
- 一次性问题
- 临时任务
- 天气
- 数学计算

如果没有值得保存的信息，仅返回：

NONE

否则：

每行输出一条长期记忆。

例如：

未来想创业做 AI SaaS

长期学习 OpenAI Agents SDK

喜欢 Go 语言        
"""
    )