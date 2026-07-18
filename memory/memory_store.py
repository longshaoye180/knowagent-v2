from memory.conversation_summary import ConversationSummary
from memory.long_memory import LongMemory
from memory.user_preference import UserPreference
from memory.user_profile import UserProfile


class MemoryStore:

    def __init__(self):
        self._memory = {
            "profile": UserProfile(),
            "preference": UserPreference(),
            "summary": ConversationSummary(),
            "long_memory": LongMemory(),
        }

    def get_profile(self):
        return self._memory["profile"]

    def set_profile(self, profile: UserProfile):
        self._memory["profile"] = profile

    def get_preference(self):
        return self._memory["preference"]

    def set_preference(self, preference: UserPreference):
        self._memory["preference"] = preference

    def get_summary(self):
        return self._memory["summary"]

    def set_summary(self, summary: ConversationSummary):
        self._memory["summary"] = summary

    def get_long_memory(self):
        return self._memory["long_memory"]

    def set_long_memory(self, long_memory: LongMemory):
        self._memory["long_memory"] = long_memory

    def set(self, key: str, value: str):
        self._memory[key] = value

    def get(self, key: str, default=None):
        return self._memory.get(key, default)

    def remove(self, key: str):
        self._memory.pop(key, None)

    def clear(self):
        self._memory.clear()

    def all(self):
        return self._memory


