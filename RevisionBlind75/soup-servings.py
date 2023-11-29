class Solution:
    def soupServings(self, n: int) -> float:
        dp = {}
        if n > 4800:
            return 1
        def helper(A,B):
   
            if A <= 0 and B <= 0:
                return 0.5
            if A <= 0 :
                return 1
            if B <= 0:
                return 0
            if (A,B) in dp:
                return dp[(A,B)]
            op1 = helper(A-100,B)
            op2 = helper(A-75,B-25)
            op3 = helper(A-50,B-50)
            op4 = helper(A-25,B-75)
            dp[(A,B)] = 0.25*(op1 + op2 + op3 + op4)
            return dp[(A,B)]
            
        return helper(n,n)
            