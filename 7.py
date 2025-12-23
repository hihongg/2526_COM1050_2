class Solution(object):
    def reverse(self, x):
        if x<0 :
            a = -1
        else:
            a = 1
        b = abs(x)
        c = a * int(str(b)[::-1])
        
        if c>= -2**31 and c <= (2**31 -1):
            return c
        else:
            return 0