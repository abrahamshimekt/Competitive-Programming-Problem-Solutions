class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i , j = 0, len(people)-1
        num_boats = 0
        people.sort()
        while i <= j:
            if people[i] + people[j] <= limit:
                num_boats +=1
                i +=1
                j -=1
            else:
                num_boats +=1
                j -=1
        return num_boats 
    
            