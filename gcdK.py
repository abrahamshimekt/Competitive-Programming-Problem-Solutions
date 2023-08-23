class Solution(object):
    def GCD(self,a,b):
        if b ==0:
            return a
        return self.GCD(b,a%b)

    def subarrayGCD(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = len(nums)
        numOfSubArrays = 0
        for left in range(N):
            currGcd = nums[left]
            for right in range(left , N):
                currGcd = self.GCD(currGcd,nums[right])
                if currGcd == k:
                    numOfSubArrays +=1
        return numOfSubArrays
       


