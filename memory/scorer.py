from memory.long_memory import MemoryItem


class MemoryScorer:

    @staticmethod
    def score(
            item: MemoryItem,
    ) -> float:

        text = item.content

        score = 0.3

        keywords = ["喜欢", "职业", "姓名","年龄","以后","长期","永远","一直","偏好","学习","目标"]

        for keyword in keywords:
            if keyword in text:
                score += 0.1

        return min(score, 1.0)