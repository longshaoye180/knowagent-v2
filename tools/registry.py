from typing import Callable


class ToolRegistry:
    """
    Tool 注册中心

    管理 Agent 可使用的工具。
    """

    def __init__(self):
        self.tools = {}


    def register(
            self,
            name: str,
            tool: Callable,
    ):
        self.tools[name] = tool


    def get(self, name: str):
        return self.tools.get(name)

    def get_tools(self, tool_names=None):
        """
        返回指定 Tool。

        tool_names=None
            返回全部 Tool（兼容旧代码）
        """

        if tool_names is None:
            return list(self.tools.values())

        result = []

        for name in tool_names:
            tool = self.get(name)

            if tool:
                result.append(tool)

        return result

