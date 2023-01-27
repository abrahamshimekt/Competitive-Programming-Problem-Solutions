n,m = input().split()
nums = [int(num) for num in input().split()]
nums.sort()
nums_count = {}
for index in range(int(n)):
    nums_count[nums[index]] = index+1
nums_count = list(nums_count.items())
if int(m) == 0:
    num = nums_count[0][0]-1
    if num >0:
       print(num)
    else:
        print(-1)
else:
    num = 0
    for num_pair in nums_count:
        if num_pair[1] == int(m):
            num = num_pair[0]
    if num:
        print(num)
    else:
        print(-1)
                
    

    
    