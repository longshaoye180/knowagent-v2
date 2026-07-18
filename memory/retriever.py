from memory.long_memory import MemoryItem
from memory.semantic_retriever import SemanticRetriever


class MemoryRetriever:

    @staticmethod
    def retrieve(
            memories: list[MemoryItem],
            query: str = "",
            top_k: int = 5,
    ) -> list[MemoryItem]:

        results = SemanticRetriever.retrieve(
            memories=memories,
            query=query,
            top_k=top_k,
        )

        results.sort(
            key=lambda item: item.importance,
            reverse=True,
        )

        return results[:top_k]
