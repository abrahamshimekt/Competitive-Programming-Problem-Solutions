borze = input()
left = 0
right = 1
number = ''
while right <= len(borze):
    if left == right:
        right +=1
    elif borze[left] == '.':
        number += '0'
        left +=1
    elif borze[right] =='.':
        number +='1'
        right +=1
        left = right
    else:
        number +='2'
        right += 1
        left = right
print(number)
        

        

