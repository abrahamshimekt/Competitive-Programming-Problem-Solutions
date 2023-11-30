from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = set()
        connected = defaultdict(lambda: float('inf'))
        n = len(equations)
        for i in range(n):
            a, b = equations[i]
            connected[(a, b)] = values[i]
            connected[(b, a)] = 1 / values[i]
            connected[(a, a)] = 1.0
            connected[(b, b)] = 1.0
            nodes.add(a)
            nodes.add(b)
        nodes = list(nodes)

        def floydWarshall():
            for k in nodes:
                for i in nodes:
                    for j in nodes:
                        connected[(i, j)] = min(connected[(i, j)], connected[(i, k)] * connected[(k, j)])

        floydWarshall()

        answer = []
        for query in queries:
            a, b = query
            value = connected[(a, b)]
            if value == float('inf') or value == 0:
                answer.append(-1.0)
            else:
                answer.append(value)

        return answer
