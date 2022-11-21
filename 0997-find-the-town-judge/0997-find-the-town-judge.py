class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n !=1 :
            return -1
        adjacencyList  = {}
        for t in trust:
            if t[0] not in adjacencyList:
                adjacencyList[t[0]] = [t[1]]
            else:
                adjacencyList[t[0]].append(t[1])
        if len(adjacencyList) < n-1:
            return -1
        judge = 0
        for person in range(1,n+1):
            if person not in adjacencyList:
                judge = person
                break
        isTrustedByAll = True
        for p in adjacencyList:
            if judge not in adjacencyList[p]:
                isTrustedByAll = False
                break
        if isTrustedByAll:
            return judge
        return -1
            
        
    
                