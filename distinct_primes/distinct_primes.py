class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        prime_factors = set()
        for num in nums:
            prime = 2
            curr_num = num
            while prime * prime <= num:
                while curr_num % prime == 0:
                    prime_factors.add(prime)
                    curr_num //= prime
                prime +=1
            if curr_num>1:
                prime_factors.add(curr_num)
                
        return len(prime_factors)


        