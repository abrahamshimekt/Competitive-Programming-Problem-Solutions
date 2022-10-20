class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j = 0, len(nums)-1
        while i <= j:
            if nums[j] == val:
                nums.pop()
                j -=1
            elif nums[i] == val:
                nums[i],nums[j] = nums[j],nums[i]
                i +=1
            else:
                i +=1