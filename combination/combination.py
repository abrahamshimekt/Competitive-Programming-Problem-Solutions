class Solution:
    def backtrack(self,result,index,path,n,k):
        # if index > n:
        if len(path) == k:
            result.append(path[:])
            return 
        # path.append(index)
        # self.backtrack(result,index+1,path,n,k)
        # path.pop()
        # self.backtrack(result,index+1,path,n,k)
        for i in range(index,n+1):
            path.append(i)
            self.backtrack(result,i+1,path,n,k)
            path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtrack(result,1,[],n,k)
        return result
      
        