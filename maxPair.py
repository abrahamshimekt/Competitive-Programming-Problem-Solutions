def minPairSum( nums):
        nums.sort()
        maxPair = 0
        i = 0
        j = len(nums) -1
        while i < j:
            maxPair = max(maxPair,nums[i] + nums[j])
            i +=1
            j -=1
        return maxPair