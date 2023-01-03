lecture_minute ,awake_minute = input().split()
thoerems = [int(theorem) for theorem in input().split()]
behavior = input().split()

# take the first n lecures as a starting or max lectures found so far
initial = sum(thoerems[:int(awake_minute)])
index  = 1
max_theorems = initial

# if the ith -1 behaviour of mishak is
#  sleep decreement the lecure at the ith - 1 time 
while index  < int(lecture_minute)-int(awake_minute)+1:
    
    if int(behavior[index-1]) == 0:
        initial -= thoerems[index-1]
    initial += thoerems[index+int(awake_minute)-1]
    max_theorems = max(max_theorems,initial)
    index +=1

print(max_theorems)




