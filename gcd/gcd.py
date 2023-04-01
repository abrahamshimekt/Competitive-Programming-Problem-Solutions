class Solution:
    def gcd(self,a,b):
        if b==0:
            return a
        return self.gcd(b,a%b)
    def findGCD(self, nums: List[int]) -> int:
        largest_num = max(nums)
        smallest_num = min(nums)
        return self.gcd(largest_num,smallest_num)

        