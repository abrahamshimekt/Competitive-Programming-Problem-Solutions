class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 1:
            return True
        init_bit = n&1
        n>>=1
        while n!=0:
            curr_last_bit = n&1
            if curr_last_bit == init_bit:
                return False
            init_bit =curr_last_bit 
            n >>=1
        return True