class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        length = len(nums)
        
        # the idea of solving this problem is to easy
        # first think that the physicall reality of what the two pointers you are going to use are
        # the fast pointer finds the unique element or element that is diffent from the element pointed 
        # pointed by the slower pointer and whenever we find an element different  it is going to be placed
        # next to the element pointed by the slow pointer
        # that is all about 

        while fast < length:
            if nums[fast] == nums[slow]:
                fast +=1   
            else:
                slow +=1
                nums[slow] = nums[fast]
                fast +=1
        return slow+1