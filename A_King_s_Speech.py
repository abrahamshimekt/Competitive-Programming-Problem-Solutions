words_num = int(input())
for index in range(words_num):
    word = input()
    output = word[:2] + '...' + word +'?'
    print(output)
