class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Identify anagrams
        anagrams = {}

        for str in strs:
            sorted_str = ''.join(sorted(str))
            if sorted_str not in anagrams:
                anagrams[sorted_str] = [str]
            else:
                anagrams[sorted_str].append(str)
        
        return list(anagrams.values())


        