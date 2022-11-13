class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        minOp = 0
        n= len(nums)
        for i in range(n):
            if nums[i] == 0:
                continue
            else:
                temp = nums[i]
                nums[i] = nums[i]-temp
                for j in range(1+i,n):
                     nums[j] = nums[j]-temp 
                minOp +=1
        return minOp
        