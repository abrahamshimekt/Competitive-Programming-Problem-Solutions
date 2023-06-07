class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def countComb(num):
            if num == 0:
                return 1
            if num < 0:
                return 0
            if num not in dp:
                count = 0
                for index in range(n):
                    count += countComb(num-nums[index])
                dp[num] = count
            return dp[num]
        return countComb(target)
