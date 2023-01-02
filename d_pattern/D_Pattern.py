num_patterns = int(input())

# create a pattern matrix
patterns = []

for pattern in range(num_patterns):
    patterns.append(input())

m = len(patterns)
n = len(patterns[0])

ans = ''

for col in range(n):
    disjoint = ''
    intersection = patterns[0][col]
    for row in range(1,m):
        # if the ith and jth char is ? pass it
        if patterns[row][col] == '?':
            continue
        # if the intersection is ? and the ith and jth char is not ? 
        # update the intersection

        elif intersection == '?':
            intersection = patterns[row][col] 
        # what assumed to be intersection is different from the ith and j th char
        # that means there is no intesection so set the intersection empty
        # and make the disjoint ?

        elif intersection != patterns[row][col] :
            disjoint = '?'
            intersection = ''
            break
    # if there is no intersection

    if intersection =='':
        ans +=disjoint
    # if there is intersection and it is ?
    elif intersection =='?':
        ans +='x'
    else:
        ans += intersection
    
print(ans)
    



