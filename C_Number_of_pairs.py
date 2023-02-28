n = int(input())
b = list(map(int,input().split()))
m  = int(input())
g = list(map(int,input().split()))
gp = 0
girls = {}
for p in g:
    if p not in girls:
        girls[p] =1
    else:
        girls[p] +=1
max_pair = 0
for i in range(n):
    curr_pair = 0
    for per in girls:
        if abs(per-b[i]) < 2:
            curr_pair += girls[per]
    max_pair = max(max_pair,curr_pair)
print(max_pair)