from typing import List, Dict
from collections import defaultdict, Counter

class Solution:
    # too slow!
    def findSubstringTooSlow(self, s: str, words: List[str]) -> List[int]:
        # O(len(s) * len(words))
        start_to_word = {}
        for i in range(len(s)):
            for word in words:
                if s[i:i+len(word)] == word:
                    start_to_word[i] = word

        result = []
        # O(len(words)
        words_counter = Counter(words)
        max_count = sum(v for v in words_counter.values())
        # O(len(s) * len(s))
        for i in range(len(s)):
            if self.is_good(i, words_counter, max_count, start_to_word):
                result.append(i)
        return result

    def is_good(self,
        i: int,
        words_counter: Dict[str, int],
        max_count: int,
        start_to_word: Dict[int, str]
    ) -> bool:
        used_words = defaultdict(lambda: 0)
        count = 0
        while count < max_count:
            word = start_to_word.get(i)
            if not word or used_words[word] >= words_counter[word]:
                return False
            count += 1
            used_words[word] += 1
            i += len(start_to_word[i])
        return True

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        return result

tests = [
    ("wordgoodgoodgoodbestword", ["word","good","best","good"], [8]),
    ("barfoothefoobarman", ["foo", "bar"], [0,9]),
]
for s, words, expected in tests:
    actual = Solution().findSubstring(s, words)
    if actual != expected:
        print(f'expected {expected}, got {actual} for findSubstring({s}, {words})')
