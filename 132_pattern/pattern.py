class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_arr = [nums[0]]
        for index in range(1,len(nums)):
            min_arr.append(min(min_arr[-1],nums[index]))
        for index in range(len(nums)-1,0,-1):
            while stack and stack[-1] <= min_arr[index-1]:
                stack.pop()
            if stack and  min_arr[index-1] < stack[-1] < nums[index]:
                return True 
            stack.append(nums[index])
        return False

        
        


        