class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10**9 + 7
        prefix = [0]*(len(nums)+1)

        for request in requests:
            
            start,end = request
            prefix[start] +=1
            prefix[end+1] -=1

        for indxx in range(1,len(nums)+1):
            prefix[indxx] += prefix[indxx-1]

        prefix.sort(reverse=True)
        nums.sort(reverse=True)

        total_sum = 0
        
        for index in range(len(nums)):
            total_sum += (nums[index]*prefix[index])%mod

        return total_sum%mod

