class Solution(object):
    def majorityElement(self, nums):
        a = {}
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
            if a[i] > len(nums)/2:
                return i
        