num_test = int(input())
for index in range(num_test):
    length = int(input())
    nums = input().split()
    transformed = input()
    is_seen = set()
    for indxx_i in range(length):
        if nums[indxx_i] not in is_seen:
            is_seen.add(nums[indxx_i])
            curr_num = nums[indxx_i]
            for indxx_j in range(indxx_i,length):
                if nums[indxx_j] == curr_num:
                    nums[indxx_j] = transformed[indxx_i]
        
    if ''.join(nums) == transformed:
        print("YES")
    else:
        print("NO")

