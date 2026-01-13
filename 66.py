class Solution(object):
    def plusOne(self, digits):
        a = int("".join(map(str,digits))) + 1
        b = list(map(int,str(a)))
        return b