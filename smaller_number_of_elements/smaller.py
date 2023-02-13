n,m = map(int,input().split())
a = input().split()
b = input().split()
first = 0
second = 0
less = 0
less_than = []
while second < m:
    if first < n and int(a[first]) < int(b[second]):
        less += 1
        first +=1
    else:
        less_than.append(less)
        second +=1
print(*less_than)