length = int(input())
nums = set(input().split())
for index in range(1,length+1):
    if str(index) not in nums:
        print(index)
