days , assistant = map(int,input().split())
availabilty = []

for index in range(assistant):
    a,b = map(int,input().split())

    availabilty.append([a,b])
prefix = [0]*(days+1)
for i in range(assistant):
    a,b = availabilty[i]
    
    prefix[a] +=1
    prefix[b+1] -=1

for j in range(1,days+1):
    prefix[j] += prefix[j-1]

no_assistant = False
for k in range(days):
    if prefix[k] == 0:
        no_assistant =True
        break
if no_assistant:
    print("YES")
else:
    print("NO")
    


