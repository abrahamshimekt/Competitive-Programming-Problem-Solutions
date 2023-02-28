n,m = map(int,input().split())
constant = int(m)-pow(int(n),2)
count = 0
for a in range(n+1):
    b = n-a*a
    if b >-1 and a+ b*b == m:
        count +=1
print(count)



    
