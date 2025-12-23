class Solution(object):
    def romanToInt(self, s):
        lama = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }
        a = 0
        for i in range(len(s)):
            if i +1 < len(s) and lama[s[i]] < lama[s[i+1]]:
                a -= lama[s[i]]
            else:
                a += lama[s[i]]
        return a