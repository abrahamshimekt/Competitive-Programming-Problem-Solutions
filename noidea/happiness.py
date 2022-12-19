n,m = input().split()
arr = input().split()
A = input().split()
B = input().split()
Ahashmap = {}
Bhashmap = {}
for numA in A:
    Ahashmap[numA] =1
for numB in B:
    Bhashmap[numB] =1
happiness = 0
for i in range(int(n)):
    if arr[i] in Ahashmap:
        happiness +=1
    elif arr[i] in Bhashmap:
        happiness -=1
print(happiness)
    
