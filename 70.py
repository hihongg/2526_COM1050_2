class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        step = [0]*(n+1)
        step[1] = 1
        step[2] = 2
        for i in range(3,n+1):
            step[i] = step[i-1] + step[i-2]
        return step[n]