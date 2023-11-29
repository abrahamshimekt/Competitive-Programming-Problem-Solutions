class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0]*101
        for log in logs:
            birth ,death = log
            years[birth-1950] +=1
            years[death-1950] -=1
        population = years[0]
        earlyYear  = 1950
        for i in range(1,100):
            years[i] = years[i-1] + years[i]
            if  years[i] > population:
                population = years[i]
                earlyYear = 1950 + i
        return earlyYear
