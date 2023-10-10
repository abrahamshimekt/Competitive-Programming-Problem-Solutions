from sys import stdin, stdout


def inp():
    return int(stdin.readline())


def inlt():
    return list(map(int, stdin.readline().strip().split()))


def insr():
    s = stdin.readline().strip()
    return list(s[:len(s)])


def invr():
    return map(int, stdin.readline().strip().split())
def bellmanFord():
    for _ in range(n - 1):
        isUpdated = False
        for u, v, w in edges:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u
                isUpdated = True
        if not isUpdated:
            break
        

    cycles = []
    for u, v, w in edges:
        if distance[u] + w < distance[v]:
            cycles.append(u)
            node = parent[u]
            while node > -1 and node != u:
                cycles.append(node)
                node = parent[node]

            cycles.append(u)
            return True, cycles[::-1]

    return False, []

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
