class Solution:
    
    def findSubsets(self,index):
        if index >=self.n:
            self.subsets.append(self.subset.copy())
            return
        self.subset.append(self.nums[index])

        self.findSubsets(index+1)
        self.subset.pop()

        self.findSubsets(index+1)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.subsets = []
        self.subset = []
        self.n = len(nums)
        self.nums = nums
        self.findSubsets(0)

        return self.subsets