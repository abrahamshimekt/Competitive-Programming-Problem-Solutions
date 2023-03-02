class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums = nums+nums
        next_greater = [0]*len(nums)
        stack = []
        has_greater = set()
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                next_greater[stack[-1]] = nums[i]
                has_greater.add(stack[-1])
                stack.pop()
            stack.append(i)
       
        for k in range(len(nums)):
            if next_greater[k] == 0 and k not in has_greater:
                next_greater[k] = -1
        return next_greater[:(len(nums)//2)]


        