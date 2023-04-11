from collections import defaultdict
cities = int(input())
adjacencyList  = defaultdict(set)
numberOfRoads = 0
for currCity in range(cities):
    row = list(map(int,input().split()))
    for otherCity in range(cities):
        if row[otherCity] == 1 and currCity not in adjacencyList[otherCity]:
            numberOfRoads +=1
            adjacencyList[currCity].add(otherCity)
print(numberOfRoads)

            

