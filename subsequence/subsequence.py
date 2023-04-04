class Solution:
    def backTrack(self,index,path):
        if index >= self.N:
            if tuple(path) not in self.visited and len(path) >1:
                self.subsequences.append(path[:])
                self.visited.add(tuple(path))
            return 
        elif  tuple(path) not in self.visited and len(path) >1:
                self.subsequences.append(path[:])
                self.visited.add(tuple(path))
        for i in range(index,self.N):
            if not path or path[-1] <= self.nums[i]:
                path.append(self.nums[i])
                self.backTrack(i+1,path)
                path.pop()
               
            
            
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.visited = set()
        self.N = len(nums)
        self.subsequences = []
        self.nums = nums
        self.backTrack(0,[])
        return  self.subsequences 

        