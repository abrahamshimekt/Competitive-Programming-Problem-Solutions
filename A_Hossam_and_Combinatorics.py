test_num = int(input())
for test in range(test_num):
    length = int(input())
    nums = [int(x) for x in input().split()]
    min_num = min(nums)
    max_num = max(nums)
    if min_num == max_num:
        print(length*(length-1))
    else:
        min_count = 0
        max_count = 0
        for index in range(length):
            if nums[index] == min_num:
                min_count +=1
            if nums[index] == max_num:
                max_count +=1
        print(min_count*max_count*2)
        