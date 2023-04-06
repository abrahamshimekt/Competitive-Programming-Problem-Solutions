class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adjacencyList = defaultdict(set)
        for road in roads:
            adjacencyList[road[0]].add(road[1])
            adjacencyList[road[1]].add(road[0])
        cityWithNeighbors = list(adjacencyList.items())
        networkRank = 0
        for i in range(len(cityWithNeighbors)):
            for j in range(i+1,len(cityWithNeighbors)):
                currNetworkRank = len(cityWithNeighbors[i][1])+ len(cityWithNeighbors[j][1])
                if cityWithNeighbors[i][0] in cityWithNeighbors[j][1]:
                    networkRank = max(networkRank,currNetworkRank-1)
                else:
                    networkRank = max(networkRank,currNetworkRank)
        return networkRank