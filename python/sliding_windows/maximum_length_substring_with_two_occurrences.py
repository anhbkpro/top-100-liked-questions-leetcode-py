from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = Counter()
        start, ans = 0, 0
        for end in range(len(s)):
            freq[s[end]] += 1
            while freq[s[end]] > 2:
                freq[s[start]] -= 1
                start += 1
            ans = max(ans, end - start + 1)

        return ans
