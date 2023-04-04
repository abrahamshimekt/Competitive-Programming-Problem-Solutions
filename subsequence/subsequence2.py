class Solution:
    def backTrack(self,index,path):
        if index >= self.N:
            if len(path) >1 and tuple(path) not in self.marked:

                self.subsequences.append(path[:])
                self.marked.add(tuple(path))
            return 
        if not path or path[-1] <= self.nums[index]:
            path.append(self.nums[index])
            self.backTrack(index+1,path)
            
            path.pop()
            
        
        self.backTrack(index+1,path)
               
            
            
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.marked = set()
        self.N = len(nums)
        self.subsequences = []
        self.nums = nums
        self.backTrack(0,[])
        return  self.subsequences 

        