class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a = nums1 + nums2
        a.sort()
        
        if (len(a))%2 != 0:
            return float(a[len(a)//2])
        else:
            b = len(a) // 2
            c = b - 1
            return (a[b] + a[c]) / 2.0