class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check length 
        if len(s) != len(t):
            return False

        # Create dicts
        dictS = {}
        dictT = {}

        # Populate dicts
        populateDict(dictS, s)
        populateDict(dictT, t)

        # Compare dicts
        return dictS == dictT
    

def populateDict(myDict: dict[s], myString: str) -> void:
    for c in myString:
        # Add newly seen letters
        if c not in myDict:
            myDict[c] = 1
        # Count up on already seen letters
        else:
            myDict[c] += 1