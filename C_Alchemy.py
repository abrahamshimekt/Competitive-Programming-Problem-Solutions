n = int(input())
t = list(map(int,input().split()))
left = 0
right = n-1
e,a = 0,0
l_t = 0
r_t = 0
while left <= right:
    if l_t <= r_t:
        e +=1
        l_t +=t[left]
        left +=1
    else: 
        a +=1
        r_t += t[right]
        right -=1
print(e,a)
    

    
    
