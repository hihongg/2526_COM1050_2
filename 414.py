class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = sorted(nums)
        if len(nums) <= 2:
            return max(nums)
        else:
            return nums[-3] 