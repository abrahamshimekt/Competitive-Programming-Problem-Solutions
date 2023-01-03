contest_num = int(input())
contests = input().split()
performance = 0

for index_i in range(contest_num-1,0,-1):
    is_greater = True
    for index_j in range(index_i-1,-1,-1):
        if int(contests[index_i]) <= int(contests[index_j]):
            is_greater = False
    if is_greater:
        performance +=1
for index_i in range(contest_num-1,0,-1):
    is_less= True
    for index_j in range(index_i-1,-1,-1):
        if int(contests[index_i]) >= int(contests[index_j]):
            is_less = False
    if is_less:
        performance +=1
print(performance)
    
        
        
