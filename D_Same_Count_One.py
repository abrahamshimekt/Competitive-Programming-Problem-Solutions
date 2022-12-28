test_num = int(input())
for index in range(test_num):
    n,m  = input().split()
    ones_count = {}
    num_ones = 0
    for indx in range(int(n)):
        test_case= [int(x) for x in input().split()]
        ones_count[indx] = sum(test_case)
        num_ones +=sum(test_case)
    num_opes = 0
    for indxx in range(int(n)):
        if ones_count[indxx] < num_ones//3:
            print(indxx+1)
            num_opes +=  num_ones//3-ones_count[indxx]
    if num_ones < int(n):
        print(-1)
    else:
        print(num_opes)

