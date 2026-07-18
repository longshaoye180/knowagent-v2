import os

from agents import Runner, Agent

from context.app_context import AppContext
from memory.conversation_summary import ConversationSummary
from service.memory_service import MemoryService


SUMMARY_TRIGGER_MESSAGE_COUNT = 4

class SummaryService:

    @staticmethod
    async def maybe_generate_summary(
            context: AppContext,
            session,
            summary_agent: Agent,
    ) -> bool:

        history = await session.get_items()

        if len(history) < SUMMARY_TRIGGER_MESSAGE_COUNT:
            return False

        await SummaryService.generate_summary(
            ctx = context,
            history = history,
            summary_agent=summary_agent
        )

        return True

    @staticmethod
    async def generate_summary(
            ctx: AppContext,
            history: list,
            summary_agent: Agent,
    ):

        history_text = "\n".join(
            [
                str(item)
                for item in history
            ]
        )

        result = await  Runner.run(
            summary_agent,
            history_text,
        )

        summary = ConversationSummary(
            summary=result.final_output
        )

        MemoryService.update_summary(
            ctx,
            summary
        )
