num_tests = int(input())

for test in range(num_tests):

    length = int(input())
    nums = input().split()
    transformed = input()
    visited = set()
    num_transformed = [0]*length
 
    # if A is made from B then B can also made from A

    for index_i in range(length):

        curr_num = nums[index_i]

        if curr_num not in visited:

            visited.add(curr_num)

            for index_j in range(index_i,length):
                if nums[index_j] == curr_num:
                    num_transformed[index_j] = transformed[index_i]

    if ''.join(num_transformed) == transformed:
        print("YES")
    else:
        print("NO")


