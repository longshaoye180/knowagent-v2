import numpy as np

from memory.embedding import EmbeddingProvider
from memory.long_memory import MemoryItem


class SemanticRetriever:

    @staticmethod
    def similarity(a, b ):
        return  np.dot(a, b)

    @classmethod
    def retrieve(
            cls,
            memories: list[MemoryItem],
            query:str,
            top_k:int=3,
    ):

        if not memories:
            return []

        query_vector = (
            EmbeddingProvider.embed(query)
        )

        results = []

        for memory in memories:

            vector = (
                EmbeddingProvider.embed(memory.content)
            )

            score = cls.similarity(query_vector, vector)

            results.append(
                (
                memory,
                score,
                )
            )

        results.sort(
            key=lambda x: x[1],
            reverse=True,
        )

        return [
            item[0] for item in results[:top_k]
        ]