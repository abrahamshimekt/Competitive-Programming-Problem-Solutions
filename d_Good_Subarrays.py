T = int(input())
for t in range(T):
    n = int(input())
    nums = list(map(int,input().split()))
    for i in range(n):
        nums[i] -=1
    for j in range(1,n):
        nums[j] += nums[j-1]

    zero_sum = defaultdict(int,{0:1})

    
