def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        n = len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    pairs +=1
                    
        return pairs
