from agents import function_tool, RunContextWrapper

from context.app_context import AppContext
from memory.user_profile import UserProfile
from service.memory_service import MemoryService


@function_tool
def remember_profile(
        wrapper: RunContextWrapper[AppContext],
        profile: UserProfile,
) -> str:
    """
        保存用户资料。

        当用户提供长期有效的信息时调用，例如：
        - 姓名
        - 年龄
        - 性别
        - 职业
        - 兴趣爱好
        """

    MemoryService.update_profile(wrapper.context, profile)

    return "Profile saved successfully."