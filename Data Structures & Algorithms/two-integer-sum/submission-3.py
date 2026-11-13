class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Without hashing, this should be O(n^2)
        # With hashing, O(n)
        for i in range(len(nums)):
            required_num = target - nums[i]
            try:
                j = nums.index(required_num)
            except ValueError: # If required not in list, move to next i
                continue
            
            # skip itself
            if j == i:
                continue

            if required_num in nums:
                return [min(i,j), max(i,j)]
    