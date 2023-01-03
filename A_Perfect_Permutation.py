num_permutations = int(input())
if num_permutations == 1:
    print(-1)
else:
    nums = []
    for index in range(1,num_permutations+1):
        nums.append(str(index))
    nums = nums[::-1]

    for indxx in range(num_permutations-1):
        if nums[indxx] == str(indxx + 1):
            nums[indxx],nums[indxx+1] = nums[indxx+1],nums[indxx] 
    nums = ' '.join(nums)
    print(nums)


