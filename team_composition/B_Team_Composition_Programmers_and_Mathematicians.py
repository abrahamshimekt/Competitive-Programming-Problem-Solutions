def isValidTeam(team,m,p):
    ms,rm,rp,ps = m//team,m%team,p%team,p//team
    rs = (rm+rp)//team
    if ms == 0 or ps ==0 or ms + ps +rs <4:
        return False
    return True
T = int(input())
for t in range(T):
    m,p = map(int,input().split())
    left = 0
    right =(m+p)//4 +1
    while right-left > 1:
        mid = left + (right-left)//2
        if isValidTeam(mid,m,p):
            left = mid
        else:
            right = mid
    print(left) 


    
    