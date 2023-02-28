n,s = map(int,input().split())
nums = list(map(int,input().split()))
left = 0
curr_sum = 0 
max_l = 0
for right in range(n+1):
    if right >=n :
        max_l = max(max_l,right-left)
        break
    if right < n:
        curr_sum += nums[right] 
    if curr_sum > s:
        max_l = max(max_l,right-left)
        curr_sum -= nums[left]
        left +=1
print(max_l)
