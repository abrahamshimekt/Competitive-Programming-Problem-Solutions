T = int(input())
for t in range(T):
    n = int(input())
    nums = list(map(int,input().split()))
    prefix = [nums[0]]
    c = 0
    for i in range(1,n):
        prefix.append(prefix[i-1] + nums[i])
    left = 0
    c = 0
    for right in range(len(nums)-1):
        while right < len(nums)-1 and  nums[left] != 0:
            if nums[right] == 0:
                c +=1
            right +=1
        if right >= len(nums)-1:
            break
        left += 1
    
    print(prefix[-2]+ c)
    