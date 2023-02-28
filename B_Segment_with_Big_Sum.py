n,s = map(int,input().split())
nums = list(map(int,input().split()))
left = 0
curr_sum = 0
segment = float('inf')
for right in range(n):
    curr_sum += nums[right]
    while curr_sum >= s:
        segment = min(segment,right-left+1)
        curr_sum -= nums[left]
        left +=1
if segment == float('inf'):
    print(-1)
else:
    print(segment)

    
