test_num = int(input())
nums = set(['0','1','2','3','4','5','6','7','8','9'])
for test in range(test_num):
    words_order = {}
    chorus = input().split()
    
    for index_i in range(len(chorus)):
        word = ''
        order = ''
        for index_j in range(len(chorus[index_i])):
            if chorus[index_i][index_j] in nums:
                order += chorus[index_i][index_j] 
            else:
                word += chorus[index_i][index_j] 
        words_order[word] = int(order)
    words_order = sorted(words_order.items(),key = lambda x:x[1])
    output = []
    for word_ordered in words_order:
        output.append(word_ordered[0])
    print(' '.join(output))



