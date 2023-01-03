username = input()
distinict_chars = set(username)
if len(distinict_chars) %2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')