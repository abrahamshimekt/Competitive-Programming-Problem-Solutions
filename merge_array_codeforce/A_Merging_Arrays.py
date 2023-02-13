n,m = map(int,input().split())
a = input().split()
b = input().split()
merged = []
i = 0
j = 0
while i < n and j < m:
    if int(a[i]) <= int(b[j]):
        merged.append(a[i])
        i +=1
    else:
        merged.append(b[j])
        j +=1
while i < n:
    merged.append(a[i])
    i +=1
while j < m:
    merged.append(b[j])
    j +=1
print(*merged)
