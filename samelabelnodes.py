from collections import defaultdict

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)

        counts = [0] * n
        visited = set()

        def dfs(node):
            visited.add(node)
            label_count = defaultdict(int)
            label_count[labels[node]] = 1

            for neighbor in graph[node]:
                if neighbor not in visited:
                    neighbor_label_count = dfs(neighbor)
                    for label, count in neighbor_label_count.items():
                        label_count[label] += count

            counts[node] = label_count[labels[node]]
            return label_count

        dfs(0)
        return counts
