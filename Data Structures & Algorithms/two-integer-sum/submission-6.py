class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Without hashing, this should be O(n^2)
        # With hashing, O(n)

        numsMap = {} # val -> index

        for i in range(len(nums)):
            value = nums[i]
            diff = target - value
            if diff in numsMap:
                return [min(numsMap[diff], i), max(numsMap[diff], i)]
            else:
                # update our hashmap for future finds
                numsMap[value] = i


    