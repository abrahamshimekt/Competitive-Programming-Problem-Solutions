class Solution:
    def orNums(self,nums):
        maxValue = 0
        for num in nums:
            maxValue |= num
        return maxValue

    def backtrack(self,start,path):
        if self.orNums(path) == self.maxValue:
            self.count +=1

        for i in range(start,self.n):
            path.append(self.nums[i])
            self.backtrack(i + 1, path)
            path.pop()



    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.maxValue = self.orNums(nums)
        self.count = 0
        self.nums = nums
        self.n = len(self.nums)
        self.backtrack(0,[])
        return self.count
       

        
