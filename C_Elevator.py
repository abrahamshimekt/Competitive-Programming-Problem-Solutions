T = int(input())
for t in range(T):
    wt,et,ef = map(int,input().split())
    w = 4*wt
    e = et*ef + et*4
    we = wt*ef + (4-ef)*et
    print(min(w,e,we))