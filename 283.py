class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a =[]
        for i in nums:
            if i != 0:
                a.append(i)
        for i in nums:
            if i == 0:
                a.append(i)
        for i in range(len(a)):
            nums[i] = a[i]
