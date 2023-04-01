def findStandingWarriors(strength,arrows):
    left = -1
    right = len(strength)
    while right-left>1:
        mid = left + (right-left)//2
        if strength[mid] > arrows:
            right = mid
        else:
            left = mid
    return right


n,q = map(int,input().split())
strength = list(map(int,input().split()))
arrows = list(map(int,input().split()))
for index in range(1,n):
    strength[index ] += strength[index-1]

curr_arrows = 0
for w in range(q):
    curr_arrows += arrows[w]
    
    if curr_arrows >= strength[-1]:
        print(findStandingWarriors(strength,curr_arrows))
        curr_arrows = 0
    else:
        print(n-findStandingWarriors(strength,curr_arrows))


