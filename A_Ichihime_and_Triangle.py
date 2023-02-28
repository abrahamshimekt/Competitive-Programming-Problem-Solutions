T = int(input().split())
a,b,c,d = map(int,input().split())
for t in range(len(T)):
    sides =[]
    for x in range(b-a+1):
        for y in range(c-b+1):
            for z in range(d-c+1):
                if a+x + b + y > c+z:
                    sides = [a+x,b+y,c+z]
                    break
                    
