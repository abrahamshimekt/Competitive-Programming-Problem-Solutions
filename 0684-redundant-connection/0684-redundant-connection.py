class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(g_set,v):
            return  v if g_set[v] == 0 else find(g_set,g_set[v])
        sets = [0]*(len(edges)+1)
        for edge in edges:
            u = find(sets,edge[0])
            v = find(sets,edge[1])
            if u == v:
                return edge
            sets[u] = v
        return []
    