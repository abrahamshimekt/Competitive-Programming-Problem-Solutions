strict_super_set = input().split()
number_of_sets = int(input())
is_super_set = True
for sets in range(number_of_sets):
    set = input().split()
    if len(set) == len(strict_super_set):
        is_super_set =False
        break
    for element in set:
        if element not in strict_super_set:
            is_super_set = False
            break
if is_super_set:
    print(True)
else:
    print(False)