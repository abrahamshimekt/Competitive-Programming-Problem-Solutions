class Solution:
    def findGCD(self, nums: List[int]) -> int:
        largestNum = max(nums)
        smallestNum = min(nums)
        def gcd(a,b):
            if a == 0:
                return b
            elif b == 0:
                return a
            elif a >= b:
                return gcd(a%b,b)
            elif a <b:
                return gcd(a, b%a)
        return gcd(largestNum,smallestNum )