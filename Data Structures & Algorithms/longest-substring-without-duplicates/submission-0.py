class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        current_length = 0
        best = 0
        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                current_length -= 1
            seen.add(s[right])
            current_length += 1
            best = max(best, current_length)
        return best
            



        