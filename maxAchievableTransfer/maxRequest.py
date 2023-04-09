class Solution:
    # the idea of solving the problem is to count the number of incoming 
    # moving transfer request whenever the transfers are balanced for certain 
    # combination of assinging people or not assigning .
    def backTrack(self,index,buildings,people):
        if index == self.N:
            for building in buildings:
                if building != 0:
                    return 
            self.maxAchievable = max(self.maxAchievable,people)
            return 
            
        buildings[self.requests[index][0]] +=1
        buildings[self.requests[index][1]] -=1

        self.backTrack(index+1,buildings,people+1)

        buildings[self.requests[index][0]] -=1
        buildings[self.requests[index][1]] +=1

        self.backTrack(index+1,buildings,people)

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.N = len(requests)
        self.maxAchievable = 0
        self.requests = requests
        buildings = [0]*n
        self.backTrack(0,buildings,0)
        return self.maxAchievable