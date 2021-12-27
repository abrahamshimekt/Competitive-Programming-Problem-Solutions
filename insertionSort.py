def insertionSort(arr):
    n = len(arr)
    temp = arr[-1]
    for i in range(0,1):
        for j in range(n-1,0,-1):
            if temp < arr[j-1]:
                arr[j] = arr[j-1]
                print(" ".join([str(x) for x in arr]))
            if temp > arr[j-1]:
                arr[j ] = temp
                print(" ".join([str(x) for x in arr]))
                break
            if j-1 ==0 and temp< arr[j-1]:
                arr[j-1] = temp
                print(" ".join([str(x) for x in arr]))
         