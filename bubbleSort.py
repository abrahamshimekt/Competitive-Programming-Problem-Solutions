def countSwaps(a):
    n = len(a)
    swapc = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j + 1],a[j]
                swapc +=1
    print("Array is sorted in %d swaps." %swapc)
    print("First Element: %d"  %a[0])
    print("Last Element: %d"  %a[-1])