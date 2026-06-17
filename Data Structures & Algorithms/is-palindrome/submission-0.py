class Solution:
    def isPalindrome(self, s: str) -> bool:
        for char in s:
            if not char.isalnum():
                s = s.replace(char, "")
        rev = s[::-1]
        return s.lower() == rev.lower()