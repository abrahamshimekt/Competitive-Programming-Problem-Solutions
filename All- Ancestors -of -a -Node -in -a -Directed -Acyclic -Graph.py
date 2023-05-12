from collections import defaultdict,deque
from sortedcontainers import SortedList
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        inDegreeCount = defaultdict(int)
        for fromi,toi in edges:
            inDegreeCount[toi] +=1

        fromTo = defaultdict(list)
        for edge in edges:
            fromi,toi = edge
            fromTo[fromi].append(toi)

        queue = deque()
        for node in range(n):
            if inDegreeCount[node]==0:
                queue.append(node)
        nodeToParent = defaultdict(set)

        while queue:
            currNode = queue.popleft()
            for neighbor in fromTo[currNode]:
                currNodeParents = nodeToParent[currNode]
                
    
                nodeToParent[neighbor] = nodeToParent[neighbor].union(currNodeParents)
                nodeToParent[neighbor].add(currNode)
                inDegreeCount[neighbor] -=1
                if inDegreeCount[neighbor] == 0:
                    queue.append(neighbor)

        answer = [0]*n
        for parent in range(n):
            answer[parent] = sorted(nodeToParent[parent])
        return answer

        

        
