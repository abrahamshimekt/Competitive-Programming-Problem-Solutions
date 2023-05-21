class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        reps = {}
        sizes = {}
        for road in roads:
            a,b,distance = road
            reps[a] = a
            reps[b] = b
           
            sizes[a] = 1
            sizes[b] = 1
        def find(city):
           
            while city != reps[city]:
                city = reps[city]

            return city
        def union(city1,city2):
            rep1 = find(city1)
            rep2 = find(city2)
           
            if sizes[rep1] < sizes[rep2]:
                reps[rep1] = rep2

            elif sizes[rep2] < sizes[rep1]:
                reps[rep2] = rep1
            else:
                reps[rep1] = rep2
                sizes[rep2] +=1
        for road in roads:
            a,b,distance = road
            union(a,b)
        minPath = float("inf")
        xrep = find(1)
        for road in roads:
            yrep = find(road[1])
            if xrep == yrep:
                minPath = min(minPath,road[2])

        
        return minPath
        
