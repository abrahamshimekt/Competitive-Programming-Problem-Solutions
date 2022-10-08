class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        if p == 1:
            return 1
        max_num = pow(2,p)-1
        power = max_num//2
        
        return (pow(max_num-1, power, 10**9 + 7) * (max_num)) % (10**9 + 7)
        
        