class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        

        def makeContribution(start,end,path):
            path.append(start)
            visited.add(start)

            if start == end:
                for node in path:
                    contri[node] +=1
                return True

            for neighbor in graph[start]:
                if neighbor not in visited and  makeContribution(neighbor,end,path):
                    return True

            path.pop()

            return False

        contri = [0] * n
        
        for start,end in trips:
            visited = set()
            makeContribution(start,end,[])
        

        dp = {}

        def dfs(node, parent, halve):
            if (node,halve) in dp:
               return dp[(node,halve)]

            result1 = float('inf')

            if not halve:
                result1 = (price[node]//2)* contri[node]
                for neighbor in graph[node]:
                    if neighbor != parent:
                        result1 += dfs(neighbor,node,True)

            result2  = price[node]*contri[node]

            for neighbor in graph[node]:
                if neighbor != parent:
                    result2 += dfs(neighbor,node,False)

            dp[(node,halve)] = min(result1,result2)

            return  dp[(node,halve)]

        return dfs(0,-1,False)
