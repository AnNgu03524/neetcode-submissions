class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # rule out different length strings
        if len(s) != len(t):
            return False
        
        # sort both strings
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        # compare
        if sorted_s == sorted_t:
            return True
        else:
            return False

        