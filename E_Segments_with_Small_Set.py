from collections import defaultdict
n,k = map(int,input().split())
nums = list(map(int,input().split()))
unique = defaultdict(int)
left = 0
good_segment = 0
for right in range(n):
    unique[nums[right]] +=1
    while len(unique) >k:
        unique[nums[left]] -=1
        if unique[nums[left]] == 0:
            del unique[nums[left]]
        left +=1
    good_segment += right -left + 1
    
print(good_segment)
    
