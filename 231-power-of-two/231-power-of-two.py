import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n==1.0:
        #     return True
        # elif n < 1 and n>0:
        #     return False
        # return self.isPowerOfTwo(n/2)
        return n and (not(n &(n-1)))
        # if n==0:
        #     return False
        # while n !=1:
        #     if n %2 != 0:
        #         return False
        #     n = n//2
        # return True
        # root =str(math.log(n,2))
        # after_decimal = ""
        # for i in range(len(root)):
        #     if root[i] ==".":
        #         after_decimal = root[i+1:]
        # if int(after_decimal) == 0:
        #     return True 
        # return False
    
                