from collections import defaultdict
n,m = input().split()
A = []
B = []
for index in range(int(n)):
    A.append(input())
for indxx in range(int(m)):
    B.append(input())
d = defaultdict(int)
for indexx in range(int(n)):
    if A[indexx] not in d:
        d[A[indexx]] = [str(indexx+1)]
    else:
        d[A[indexx]].append(str(indexx+1))

for char in B:
    index =d.get(char,-1)
    if index ==-1:
        print(-1)
    else:
        print(' '.join(index))