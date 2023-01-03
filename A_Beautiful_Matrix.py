ones_place  = (0,0)
for index_i in range(5):
    row = input().split()
    for index_j in range(5):
        if int(row[index_j]) == 1:
            ones_place = (index_i,index_j)
operations = abs(ones_place[0] - 2) + abs(ones_place[1]-2)
print(operations)


