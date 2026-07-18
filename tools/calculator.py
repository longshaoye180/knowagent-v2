from agents import function_tool


@function_tool
def calculate(expression: str) -> str:
    """
    计算数学表达式
    """

    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"计算失败：{e}"