class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum = max(nums)
        twice = True
        index = 0
        for i in range(len(nums)):
            if nums[i] == maxNum:
                index = i
            elif nums[i] *2 > maxNum:
                    twice = False
            else:
                continue
        return index if twice else -1
                    
                
                
            
            
        