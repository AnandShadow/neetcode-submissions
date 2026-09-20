class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_nums= {}
        for i, n in enumerate(nums):
            diff= target - n
            if diff in seen_nums:
                return [seen_nums[diff], i]
            seen_nums[n]=i
        return [-1,-1]
