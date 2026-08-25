class Solution:
    def count_differences(self, word1: str, word2: str) -> int:
        if len(word1) != len(word2):
            return -1
        return sum(1 for i in range(len(word1)) if word1[i] != word2[i])

    def ladderLength(self, start: str, end: str, word_list: list[str]) -> int:
        word_set = set(word_list)

        if end not in word_set or not word_set or len(start) != len(end):
            return 0

        queue = [(start, 1)]
        visited = {start}

        while queue:
            next_queue = []
            for word, steps in queue:
                if word == end:
                    return steps

                for candidate in word_list:
                    if (self.count_differences(word, candidate) == 1 and
                            candidate not in visited):
                        visited.add(candidate)
                        next_queue.append((candidate, steps + 1))

            queue = next_queue

        return 0