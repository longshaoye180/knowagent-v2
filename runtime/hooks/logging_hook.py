from typing import Any

from runtime.hooks.base import BaseHook
from runtime.logger import RuntimeLogger


class LoggingHook(BaseHook):

    async def on_request_start(self, context: Any):
        RuntimeLogger.title("Request Start")
        RuntimeLogger.info(context.current_query)


    async def on_request_end(self, context: Any):
        RuntimeLogger.title("Request End")