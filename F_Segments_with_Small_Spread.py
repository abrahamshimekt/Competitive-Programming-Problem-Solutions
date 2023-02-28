n,k = map(int,input().split())
nums = list(map(int,input().split()))
min_num = float('inf')
max_num = 0
left = 0
for right in range(n):
    while max_num - min_num > k:
        
