class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        length = len(nums)
        
        while fast < length:
            if nums[fast] == nums[slow]:
                fast +=1   
            else:
                slow +=1
                nums[slow] = nums[fast]
                fast +=1
        return slow+1