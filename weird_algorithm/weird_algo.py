number = int(input())
ans = ''
while number != 1:
    if number %2 == 0:
        ans +=f'{number} '
        number = number//2
        
    else:
        ans +=f'{number} '
        number = number*3 + 1
ans += '1'
        
print(ans)
