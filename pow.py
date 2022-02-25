class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.myPow(x,-n)
        val = self.myPow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x
        
#         if n >= 0:
#             if n == 0:
#                 return 1
#             else:
#                 return x*self.myPow(x,n-1)
#         else:
#             if n ==0:
#                 return 1
#             else:
#                 return (1/x)*self.myPow(x,n + 1)
        