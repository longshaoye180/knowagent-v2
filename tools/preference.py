from agents import function_tool, RunContextWrapper

from context.app_context import AppContext
from memory.user_preference import UserPreference
from service.memory_service import MemoryService


@function_tool
def remember_preferences(
        wrapper: RunContextWrapper[AppContext],
        preference: UserPreference,
) -> str:

    MemoryService().update_preference(
        wrapper.context,
        preference
    )

    return "Preferences saved successfully"