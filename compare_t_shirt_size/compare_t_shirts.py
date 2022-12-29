num_tests = int(input())
for test in range(num_tests):
    T_shirt_a, T_shirt_b = input().split()
    if T_shirt_a[-1] != T_shirt_b[-1] :
        if T_shirt_a[-1] == 'L' and (T_shirt_b[-1] == 'S' or  T_shirt_b[-1] == 'M'):
            print(">") 
        elif T_shirt_a[-1] == 'M' and T_shirt_b[-1] == "S":
            print('>')
        elif T_shirt_a[-1] == 'M' and T_shirt_b[-1] == "L":
            print('<')
        elif T_shirt_a[-1] == "S" and (T_shirt_b[-1] == "L" or  T_shirt_b[-1] == "M"):
            print('<')
    else:
        if len(T_shirt_a[-1]) == len(T_shirt_b[-1]):
            print('=')

        elif T_shirt_a[-1] == 'S':
            if len(T_shirt_a) > len(T_shirt_b):
                print('<')
            else:
                print('>')
                
        elif T_shirt_a[-1] == 'L':
            if len(T_shirt_a) > len(T_shirt_b):
                print('>')
            else:
                print('<')