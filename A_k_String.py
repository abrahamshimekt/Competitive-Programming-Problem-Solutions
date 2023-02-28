k = int(input())
s = input()
char_count = {}
for index in range(len(s)):
    if s[index] not in char_count:
        char_count[s[index]] =1
    else:
        char_count[s[index]] +=1
reordered = []
flag = False
for char in char_count:
    if char_count[char] % k !=0:
        flag = True
        break
    else:
        reordered.append(char*char_count[char])
if flag:
    print(-1)
else:
    print(''.join(reordered))
