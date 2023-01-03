test_num = int(input())
for test in range(test_num):
    length = int(input())
    tower = input().split()
    blocks_at_1 = int(tower[0])
    for index in range(1,length):
        if int(tower[index]) > blocks_at_1:
           blocks_at_1 +=  ((int(tower[index])-blocks_at_1)//2) + 1
        else:
            continue
    print(blocks_at_1)


