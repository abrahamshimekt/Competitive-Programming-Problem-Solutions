T = int(input())
for t in range(T):
    n = int(input())
    nums =list(map(int, input().split()))
    sign = '+'
    if nums[0] < 0:
        sign = "-"
    index = 0
    max_num = float('-inf')
    max_sum = 0
    while index <=n:
        curr_sign = "-"
        if index < n and nums[index] > 0:
            curr_sign = "+"
        if index < n and curr_sign == sign:
            max_num = max(max_num,nums[index])
            index +=1
        else:
            max_sum += max_num
            if index < n:
                max_num = nums[index]
            sign = curr_sign
            index +=1
    print(max_sum)




        

