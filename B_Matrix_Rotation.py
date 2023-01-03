test_num = int(input())
for test in range(test_num):
    mat = []
    row1 = input().split()
    row2 = input().split()
    mat = [row1,row2]
    is_beautiful = False
    for index in range(4):
        is_row_valid = (int(mat[0][0]) < int(mat[0][1]) and int(mat[1][0]) < int(mat[1][1]))
        is_col_valid = (int(mat[0][0]) < int(mat[1][0]) and int(mat[0][1]) < int(mat[1][1]))
        if  is_row_valid and is_col_valid:
            is_beautiful = True
            break
        else:
            row1 = [mat[1][0],mat[0][0]]
            row2 = [mat[1][1],mat[0][1]]
            mat = [row1,row2]
    if is_beautiful:
        print('YES')
    else:
        print("NO")

            

    