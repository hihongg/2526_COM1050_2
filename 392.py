class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = 0
        for i in t:
            if a < len(s) and i == s[a]:
                a += 1
        return a == len(s)