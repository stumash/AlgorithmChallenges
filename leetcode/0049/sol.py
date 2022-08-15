from collections import Counter, defaultdict
from typing import Dict, List

class Solution:
    def counter_to_key(self, c: Counter[str]) -> str:
        result = ''
        for ch in map(chr, range(ord('a'), ord('z')+1)):
            result += f'{c[ch]}#'
        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_count_to_word: Dict[str, List[str]] = defaultdict(list)
        for s in strs:
            key = self.counter_to_key(Counter(s))
            freq_count_to_word[key].append(s)
        return list(freq_count_to_word.values())

if __name__ == "__main__":
    tests = [
        (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]])
    ]
    for s, ans in tests:
        print(Solution().groupAnagrams(s))
        print(ans)
