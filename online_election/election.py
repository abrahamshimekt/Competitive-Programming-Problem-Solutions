class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.freq = defaultdict(int,{self.persons[0]:1})
        curr_max = self.persons[0]
        for index in range(1,len(self.persons)):
            self.freq[self.persons[index]] +=1
            if self.freq[self.persons[index]] >= self.freq[curr_max]:
                curr_max = self.persons[index]
            self.persons[index] = curr_max
       
    def find_leading(self,times,t):
        left = -1
        right = len(self.persons)
        while right -left >1 :
            mid = left + (right-left)//2
            if  times[mid]<= t:
                left = mid
            else:
                right = mid
        return left

    def q(self, t: int) -> int:
        index = self.find_leading(self.times,t)
        
        return self.persons[index]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)