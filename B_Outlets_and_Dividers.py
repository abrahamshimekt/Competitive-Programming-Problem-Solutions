T = int(input())
for t in range(T):
    n,m = map(int,input().split())
    outlets = list(map(int,input().split()))
    outlets.sort(reverse=True)
    drive = 2
    count = 0
    for o in range(m):
        if drive >= n:
            break
        else:
            count +=1
        drive += outlets[o]-1
    if drive < n:
        print(-1)
    else:
        print(count)

