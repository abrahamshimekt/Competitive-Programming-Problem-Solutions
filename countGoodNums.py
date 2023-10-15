class Solution:

    def multiply(self,a,b,mod):
        return ((a%mod)*(b%mod))%mod
   
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        odds = n//2
        evens = n-odds
        oddComb = pow(4,odds,mod)
        evenComb = pow(5,evens,mod)
        return self.multiply(oddComb,evenComb,mod)





        

        
