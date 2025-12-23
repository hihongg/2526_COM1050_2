class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        a = []
        for i in s:
            if i in pair:
                b = a.pop()
                if b != pair[i]:
                    return False
            else:
                a.append(i)
        if len(a) == 0:
            return True
        else:
            return False
