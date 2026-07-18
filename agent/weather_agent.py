import os

from agents import Agent

from context.app_context import AppContext
from models.weather_result import WeatherResult
from tools.registry import ToolRegistry


def create_weather_agent(
        registry: ToolRegistry,
) -> Agent[AppContext]:
    """
    天气专家 Agent
    """

    return Agent(
        name="Weather Agent",
        handoff_description="""
        处理所有天气相关的问题。

包括：

- 天气
- 温度
- 下雨
- 晴天
- 阴天
- 穿衣建议
        """,
        instructions="""
你是一位天气助手。

必须调用 get_weather 工具。

不能自己编造天气。

最终返回结构化天气信息。        
""",
        model=os.getenv("LLM_MODEL"),
        tools=registry.get_tools(["weather"]),
        output_type=WeatherResult,
    )