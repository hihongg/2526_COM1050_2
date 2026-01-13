class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        s = 0
        while l < r:
            h = min(height[l],height[r])
            cd = r - l
            a = h*cd
            s = max(s,a)
            if height[l] < height[r]:
                l += 1
            else:
                r -=1
        return s