borze = input()
left = 0
number = ''
for right in range(1,len(borze)+1):
    if left == right:
       continue
    elif borze[left] == '.':
        number += '0'
        left +=1
    elif borze[right] =='.':
        number +='1'
        left = right+1
    else:
        number +='2'
        left = right+1

print(number)