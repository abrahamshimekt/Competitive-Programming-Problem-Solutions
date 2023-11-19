class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = defaultdict(int)
        for i in range(len(nums)):
            if target -nums[i] in freq:
                return [freq[target-nums[i]],i]
            else:
                freq[nums[i]] = i
            

        
        
