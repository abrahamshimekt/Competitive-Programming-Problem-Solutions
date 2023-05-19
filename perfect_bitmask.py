Tc = int(input())
for tc in range(Tc):
    num = int(input())
    if num < 3:
        print(3)
    elif num % 2 == 1:
        print(1)
    else:
       res = num&-num
       if res == num:
           print(res + 1)
       else:
           print(res)
