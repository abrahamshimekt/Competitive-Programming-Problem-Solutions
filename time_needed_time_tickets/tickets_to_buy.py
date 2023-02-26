class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = k+1
        for index in range(k+1):
            tickets[0]-=1
            tickets.append(tickets.pop(0))
        indxx = 0
        while indxx < len(tickets):
            if tickets[-1] == 0:
                break
            elif tickets[indxx] == 0:
                indxx +=1
            else:
                tickets[indxx] -=1
                time +=1
                indxx = (indxx + 1)%len(tickets)
        return time
        
        