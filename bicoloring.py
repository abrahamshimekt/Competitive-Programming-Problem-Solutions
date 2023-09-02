from collections import defaultdict,deque

def is_bicolorable(N, E):
    if N == 0:
        return False

    graph = defaultdict(list)
    colors = [-1] * (N + 1)

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    start_node = 1
    colors[start_node] = 0

    queue = deque()
    queue.append(start_node)

    while queue:
        node = queue.popleft()
        current_color = colors[node]

        for neighbor in graph[node]:
            if colors[neighbor] == -1:
                colors[neighbor] = 1 - current_color
                queue.append(neighbor)
            elif colors[neighbor] == current_color:
                return False

    return True

# Read input and process multiple test cases
while True:
    N= int(input())
    if N == 0:
        break

    E = int(input())
    if is_bicolorable(N, E):
        print("BICOLOURABLE.")
    else:
        print("NOT BICOLOURABLE.")
