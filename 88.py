class Solution(object):
    def merge(self, nums1, m, nums2, n):
        a =[]
        i = 0
        j = 0
        while i < m:
            a.append(nums1[i])            
            i += 1
        while j < n:
            a.append(nums2[j])
            j += 1
        a.sort()
        for i in range(m+n):
            nums1[i] = a[i]