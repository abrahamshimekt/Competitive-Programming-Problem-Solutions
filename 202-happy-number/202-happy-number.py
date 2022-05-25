from collections import Counter
class Solution:
    def isHappy(self, n: int) -> bool:
        num_dic = { 1:1 }
        while n not in num_dic:
            num_dic[n] = 1
            n = sum(i **2 for i in map(int, str(n)))
        return n == 1