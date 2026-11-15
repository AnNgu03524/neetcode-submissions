class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a set nums for lookup
        numsSet = set(nums)

        for i in range(len(nums)):
            diff = target - nums[i] # required num to complete the twosum
        
            if diff in numsSet:     # O(1) lookup
                j = nums.index(diff)

                if i == j:  # exclude itself
                    continue

                return [min(j, i), max(j, i)] # + O(n) only fires once



        