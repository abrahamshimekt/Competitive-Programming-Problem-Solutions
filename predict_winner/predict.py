class Solution:
    def winner(self,nums,left,right,turn):
        if left > right:
            return 0
        if turn :
            return max(nums[left]+self.winner(nums,left+1,right,False),nums[right]+self.winner(nums,left,right-1,False))
        else:
            return min(self.winner(nums,left+1,right,True),self.winner(nums,left,right-1,True))
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        total = sum(nums)
        score = self.winner(nums,0,len(nums)-1,1)
        return score >= total-score
        
        

        
        