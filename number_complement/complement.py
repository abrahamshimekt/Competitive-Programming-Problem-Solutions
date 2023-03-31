class Solution:
    def findComplement(self, num: int) -> int:
        N = num.bit_length()
        for x in range(N):
            num = num^(1<<x)
        return num
       
