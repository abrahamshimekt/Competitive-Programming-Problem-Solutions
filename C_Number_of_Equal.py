from collections import Counter
n,m = map(int,input().split())
a = Counter(list(map(int,input().split())))
b = Counter(list(map(int,input().split())))
goods = 0
for num in a:
    goods += b.get(num,0)*a[num]
print(goods)
