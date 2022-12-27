n,m = input().split()
A = []
B = []
for index in range(int(n)):
    A.append(input())
for indxx in range(int(m)):
    B.append(input())
for char in B:
    indexes = ''
    for indexx in range(int(n)):
        if A[indexx] == char:
            indexes += f'{indexx+1} '
    if indexes == '':
        print(-1)
    else:
        print(indexes)