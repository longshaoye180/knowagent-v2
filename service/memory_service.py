from datetime import datetime

from context.app_context import AppContext
from memory.conversation_summary import ConversationSummary
from memory.long_memory import MemoryItem
from memory.scorer import MemoryScorer
from memory.user_preference import UserPreference
from memory.user_profile import UserProfile


class MemoryService:

    @staticmethod
    def update_profile(
            context: AppContext,
            profile: UserProfile,
    ):
        current = context.memory.get_profile()

        if profile.name is not None:
            current.name = profile.name

        if profile.age is not None:
            current.age = profile.age

        if profile.gender is not None:
            current.gender = profile.gender

        if profile.job is not None:
            current.job = profile.job

        if profile.hobbies:
            hobbies = set(current.hobbies)

            hobbies.update(profile.hobbies)

            current.hobbies = sorted(hobbies)

        context.memory.set_profile(current)

    @staticmethod
    def get_profile(context: AppContext) -> UserProfile:
        return context.memory.get_profile()

    @staticmethod
    def get_preference(context: AppContext) -> UserPreference:
        return context.memory.get_preference()

    @staticmethod
    def update_preference(
            context: AppContext,
            preference: UserPreference,
    ):

        current_preference = context.memory.get_preference()
        if preference.language is not None:
            current_preference.language = preference.language

        if preference.response_style is not None:
            current_preference.response_style = preference.response_style

        if preference.code_style is not None:
            current_preference.code_style = preference.code_style

        context.memory.set_preference(current_preference)

    @staticmethod
    def get_summary(context: AppContext) -> ConversationSummary:
        return context.memory.get_summary()

    @staticmethod
    def update_summary(context: AppContext, summary: ConversationSummary):
        current = context.memory.get_summary()

        if summary.summary is not None:
            current.summary = summary.summary

        context.memory.set_summary(current)


    @staticmethod
    def remember(
            context: AppContext,
            content: str,
    ):
        memory = (
            context.memory.get_long_memory()
        )

        item = MemoryItem(
                content=content,
            )

        item.importance = MemoryScorer.score(item)

        memory.memories.append( item )

        context.memory.set_long_memory(memory)


    @staticmethod
    def consolidate(context: AppContext):
        memory = (
            context.memory.get_long_memory()
        )

        unique = {}

        for item in memory.memories:

            key = item.content.strip().lower()

            if key not in unique:
                unique[key] = item
                continue

            if item.importance > unique[key].importance:
                unique[key] = item

        memory.memories = list(unique.values())

        context.memory.set_long_memory(memory)


    @staticmethod
    def decay(
            context: AppContext,
            days: int = 30,
            decay_rate: float = 0.05,
    ):
        memory = context.memory.get_long_memory()

        now = datetime.utcnow()

        remained = []

        for item in memory.memories:

            age = now - item.updated_at

            period = age.days // days

            importance = max(0, item.importance - period * decay_rate)

            item.importance = importance

            if importance > 0.2:
                remained.append(item)

        memory.memories = remained

        context.memory.set_long_memory(memory)

