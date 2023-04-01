n = int(input())
names = list(input().split())
q = int(input())
qrs = []
for i in range(q):
    qrs.append(input())
    
for qs in qrs:
    left = -1
    right = n
    while right - left >1:
        mid = left + (right-left)//2
        if names[mid] >qs:
            right = mid
        else:
            left = mid
    print(right)
