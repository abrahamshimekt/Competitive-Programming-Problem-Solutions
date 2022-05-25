from collections import Counter
class Solution:
    def isHappy(self, n: int) -> bool:
        s = { 1 }
        while n not in s:
            s.add(n)
            n = sum(i * i for i in map(int, str(n)))
        return n == 1