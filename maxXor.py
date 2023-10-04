
class Solution:
    def __init__(self):
        self.root = {}
    def insert(self,num,bitLength):
        curr = self.root
        for i in range(bitLength, -1, -1):
            ithBit = (num >> i) & 1
            if ithBit not in curr:
                curr[ithBit] = {}
            curr = curr[ithBit]
            
    def findMaxXor(self,num,bitLength):
        curr = self.root
        maxXor = 0
        for i in range(bitLength, -1, -1):
            ithBit = (num >> i) & 1
            if 1 - ithBit in curr:
                maxXor |= 1 << i
                curr = curr[1 - ithBit]
            else:
                curr = curr[ithBit]
        return maxXor
                
        
        
    def findMaximumXOR(self, nums: List[int]) -> int:
        bitLength = max(nums).bit_length()
        for num in nums:
            self.insert(num,bitLength)
            
        maxXor = 0
        for num in nums:
            maxXor = max(maxXor,self.findMaxXor(num,bitLength))
            
        return maxXor
        
            
