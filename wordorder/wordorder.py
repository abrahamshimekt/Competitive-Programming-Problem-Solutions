x = int(input())
word = [input() for i in range(x)]
freq = {}
for w in word:
    if w not in freq:
        freq[w] =1
    else:
        freq[w] +=1
print(len(freq))
for wrd in freq:
    print(freq[wrd],end=' ')