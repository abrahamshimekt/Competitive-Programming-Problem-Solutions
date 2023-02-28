n = int(input())
nums = list(map(int,input().split()))
nums.sort()

i = 0
j = 0
max_l = 0
while j<=n :
    if j < n and nums[j]-nums[i] < 6:
        j +=1
    else:
        max_l = max(max_l,j-i)
        if j == n:
            break
        i +=1
print(max_l)
