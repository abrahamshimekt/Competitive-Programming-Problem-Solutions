def countSwaps(a):
    # Write your code here
    length = len(a)
    swaps = 0
    for index_i in range(length):
        for index_j in range(length-1-index_i):
            if a[index_j] > a[index_j+1]:
                a[index_j],a[index_j+1] = a[index_j+1],a[index_j]
                swaps +=1
    print("Array is sorted in {} swaps.".format(swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))