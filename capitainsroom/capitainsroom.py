x = int(input())
rooms = input().split()
family_size = {}
for family in rooms:
    if family not in family_size:
        family_size[family] =1
    else:
         family_size[family] +=1
for f in family_size:
    if family_size[f] == 1:
        print(f)
    