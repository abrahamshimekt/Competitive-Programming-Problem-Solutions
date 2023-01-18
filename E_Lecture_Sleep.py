lecture_minute ,awake_minute = input().split()
thoerems = [int(theorem) for theorem in input().split()]
behavior = input().split()

# take the first n lecures as a starting or max lectures found so far

initial = 0
for index in range(int(lecture_minute)):
    if int(behavior[index] ) == 1:
        initial += int(thoerems[index])
    
max_theorems = initial

# if the ith -1 behaviour of mishak is
#  sleep decreement the lecure at the ith - 1 time 

left = 0

for right in range(int(lecture_minute)):
    if int(thoerems[right]) == 0:
        initial += int(thoerems[right])
    if right - left > int(awake_minute):
        if int(thoerems[left]) == 0:
            initial -= int(thoerems[left])
        left +=1
    max_theorems = max(max_theorems,initial)
        

print(max_theorems)




