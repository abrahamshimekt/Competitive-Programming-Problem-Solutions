class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum//2
        n = len(stones)
        dp = {}
        def helper(start,currSum):
            if currSum >= target or start == n:
                return abs(2*currSum-stoneSum)

            if (start,currSum) in dp:
                return dp[(start,currSum)]

            taken = helper(start+1,currSum + stones[start])

            notTaken = helper(start+1,currSum)

            dp[(start,currSum)] = min(taken,notTaken)
            return dp[(start,currSum)]
        return helper(0,0)



