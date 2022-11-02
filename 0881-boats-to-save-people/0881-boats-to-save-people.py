class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i , j = 0, len(people)-1
        num_boats = 0
        sorted_people = sorted(people)
        while i <= j:
            if sorted_people[i] + sorted_people[j] <= limit:
                num_boats +=1
                i +=1
                j -=1
            else:
                num_boats +=1
                j -=1
        return num_boats 
    
            