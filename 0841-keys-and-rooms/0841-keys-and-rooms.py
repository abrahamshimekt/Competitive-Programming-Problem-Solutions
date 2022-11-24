class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = []
        for key in rooms[0]:
            keys.append(key)
        visited = {0:1}
        for key in keys:
            if key not in visited:
                newkeys  = rooms[key]
                visited[key] = 1
                for k in newkeys:
                    if k not in visited and k not in keys:
                        keys.append(k)
        n = len(rooms)
        for i in range(n):
            if i not in visited:
                return False
        return True
                
            
            
        