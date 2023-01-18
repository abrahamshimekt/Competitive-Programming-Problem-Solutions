def insertionSort1(n, arr):
    # Write your code here
    for index_ in range(n):
        arr[index_] = str(arr[index_])
        
    curr_num = arr[-1]
    for index in range(n-2,-1,-1):
        if index == 0 and int(arr[index]) > int(curr_num) :
           
            arr[index+1] = arr[index]
            print(' '.join(arr))
            arr[index] =curr_num 
            print(' '.join(arr))
        elif int(arr[index]) > int(curr_num):
            arr[index+1] = arr[index]
            print(' '.join(arr))
        else:
            arr[index+1] = curr_num
            print(' '.join(arr))
            break
            