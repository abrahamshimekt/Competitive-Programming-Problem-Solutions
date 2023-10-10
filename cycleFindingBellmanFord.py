from sys import stdin, stdout

def invr():
    return map(int, stdin.readline().strip().split())
def bellmanFord():
    isUpdated = False
    for _ in range(n):
        isUpdated = False
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u
                isUpdated = True
                x = v
        if not isUpdated:
            break
    if  not isUpdated:
        return False,[]
    else:
        for i in range(n):
            x = parent[x]
        v = x
        cycles = []
        while True :
            cycles.append(v)
            if x == v and len(cycles) > 1:
                break
            v = parent[v]
        
        return True, cycles[::-1]

n, m = invr()
edges = []
for _ in range(m):
    u, v, w = invr()
    edges.append((u, v, w))

distance = [0] * (n + 1)
parent = [-1] * (n + 1)

hasCycle, cycle = bellmanFord()
if hasCycle:
    print("YES")
    print(*cycle)
else:
    print("NO")
