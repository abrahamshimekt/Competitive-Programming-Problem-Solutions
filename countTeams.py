class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        for i in range(n):
            leftSmaller=leftLarger=rightSmaller=rightLarger = 0
            for j in range(i):
                if rating[j] < rating[i]:
                    leftSmaller +=1
                if rating[j] > rating[i]:
                    leftLarger +=1
            for k in range(i+1,n):
                if rating[k] < rating[i]:
                    rightSmaller +=1
                if rating[k] > rating[i]:
                    rightLarger +=1
            count += leftSmaller*rightLarger + leftLarger*rightSmaller
        return count
                

                    
