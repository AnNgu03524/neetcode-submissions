class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # rule out different length strings
        if len(s) != len(t):
            return False
        
        # sort both strings
        s = sorted(s)
        t = sorted(t)

        # compare
        if s == t:
            return True
        else:
            return False

        