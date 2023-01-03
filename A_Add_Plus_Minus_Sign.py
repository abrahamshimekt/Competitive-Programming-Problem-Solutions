test_num = int(input())
for test in range(test_num):
    length = int(input())
    nums = input()
    total = int(nums[0])
    expression = ''
    for index in range(1,length):
        if total+int(nums[index]) <= abs(total-int(nums[index])):
            expression +='+'
            total += int(nums[index])
        else:
            expression +='-'
            total -= int(nums[index])
    print(expression)


