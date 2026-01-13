class Solution(object):
    def lengthOfLastWord(self, s):
        a = list(s.split())
        b = list(a[-1])
        return len(b)
        