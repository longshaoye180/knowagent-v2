from typing import Any

from agents import function_tool, RunContextWrapper

from context.app_context import AppContext


@function_tool
def get_weather(
        wrapper: RunContextWrapper[AppContext],
        city: str
) -> dict[str, Any]:
    """
    查询城市天气
     Args:
         City:
            城市名称
    """

    current_user= wrapper.context.current_user

    fake_weather = {
        "北京": "今天晴，温度25度",
        "上海": "今天多云，温度28度",
        "深圳": "今天小雨，温度30度",
    }

    weather = fake_weather.get(city, f"{city}天气未知")

    # return f"{current_user},{city},{weather}"
    return {
        "user": current_user,
        "city": city,
        "weather": weather
    }