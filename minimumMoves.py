class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        moves =0
        nums.sort()
        pre = nums[0]
        for i in range(1,len(nums)):
            curr = nums[i]
            if curr <= pre:
                moves += pre - curr +1
                curr = pre +1
            pre = curr
        return moves
        
#         moves = 0
#         unique = [0]*len(nums)
#         while len(set(nums)) < len(nums):
#             for i in range(len(nums)):
#                 if nums[i] ==0 and i==0:
#                     unique[i] =0
#                 elif nums[i] not in unique :
#                     unique[i] = nums[i]
#                 else:
#                     unique[i] = nums[i] +1
#                     moves +=1
                    
#             nums = unique
#             unique = [0]*len(nums)
            
#         return moves
        