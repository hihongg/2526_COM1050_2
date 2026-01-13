class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        a ={}
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        for k,v in a.items():
            if v == 1:
                return k