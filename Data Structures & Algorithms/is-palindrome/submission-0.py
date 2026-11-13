class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        mid = len(s) // 2
        L = 0
        R = len(s) - 1
        while(True):
            if (L > mid) or (R < mid):
                break
            if s[L] != s[R]:
                return False
            else:
                L += 1
                R -= 1
        return True
