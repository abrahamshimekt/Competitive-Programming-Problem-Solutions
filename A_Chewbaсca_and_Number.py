num =list(input())
for i in range(len(num)):
    if int(num[i]) ==9 and i==0:
        continue
    elif int(num[i]) > 9-int(num[i]):
        num[i] = str(9-int(num[i]))
print("".join(num))

