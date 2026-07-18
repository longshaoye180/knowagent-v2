from dataclasses import dataclass

from memory.memory_store import MemoryStore


@dataclass
class AppContext:
    """
    应用运行上下文。

    后续会逐步加入：
    - 当前用户
    - 数据库
    - Redis
    - Trace ID
    """

    memory: MemoryStore

    current_query: str = ""