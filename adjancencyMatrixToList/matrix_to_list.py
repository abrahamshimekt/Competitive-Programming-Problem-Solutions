from collections import defaultdict

N = int(input())
addjacency_list = defaultdict(list)

for i in range(N):
    row = input().split()
    for j in range(N):
        if row[j] == "1":
            addjacency_list[i+1].append(j+1)
for node in addjacency_list:
    print(len(addjacency_list[node]),*addjacency_list[node])

