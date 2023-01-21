tests = int(input())

for test in range(tests):
    
    length = int(input())
    nums = list(map(int,input().split()))

    nums.sort()
    removed_count = 0

    for index in range(length-1):

        if nums[index+1]-nums[index] <=1:
            removed_count +=1

    if length - removed_count == 1:
        print("YES")

    else:
        print("No")
            
    
    
    
    