n = int(input())
nums = list(map(int,input().split()))
i = 0
j = 1
max_l = 1
curr_num = nums[0]
while j <= n:
    if j < n and nums[j] >= curr_num:
        curr_num = nums[j]
        j +=1
    else:
        max_l = max(max_l,j-i)
        i = j
        if j < n:
            curr_num = nums[j]
        j += 1
print(max_l)
    


    


    

    






