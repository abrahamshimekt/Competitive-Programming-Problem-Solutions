class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1 or x == 0 or n == 1:
            return x
        elif x == -1:
            if n % 2 == 0:
                return 1
            else:
                return -1
        elif n==0:
            return 1
        elif n < 0:
            return 1/(self.myPow(x,-n)) 
        # we can express the power of x to n as (x**a)**2 if 2a = 0 or x(x**a)**2 
        # so first we need to find the power of x to a then we square it 
        val = self.myPow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x
        
        
        
        
        
        