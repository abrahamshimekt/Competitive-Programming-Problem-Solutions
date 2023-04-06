from collections import defaultdict

N = int(input())
K = int(input())
adjacencyList = defaultdict(list)
for i in range(K):

    
    operation = input().split()
  

    if len(operation) == 3:

        adjacencyList[operation[1]].append(operation[2])
        adjacencyList[operation[2]].append(operation[1])
    else:
        print(*adjacencyList[operation[1]])

