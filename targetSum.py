class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def findTarget(index,currSum):
            if index >= n:
                return currSum == target
            
            if (index,currSum) not in dp:
                dp[(index,currSum)] = findTarget(index+1,currSum-nums[index]) + findTarget(index+1,currSum+nums[index])
            return dp[(index,currSum)]
        return findTarget(0,0)
