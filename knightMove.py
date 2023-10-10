class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7
        graph = {
        0:(4,6),
        1:(6,8),
        2:(7,9),
        3:(4,8),
        4:(0,3,9),
        5:(),
        6:(0,1,7),
        7:(2,6),
        8:(1,3),
        9:(2,4)
    }
        currCounts = [1]*10
        for i in range(n-1):
            nextCounts = [0]*10
            for j in range(10):
                for neighbor in graph[j]:
                    nextCounts[neighbor] += currCounts[j]
                    nextCounts[neighbor] %= mod
            currCounts = nextCounts
        return sum(currCounts) %mod
