class Solution(object):
    def isPowerOfThree(self, n):
        a = []
        if n <= 0:
            return False
        else:
            for i in range(0,20):
                if n == 3**i:
                    a.append(i)
        return bool(a)