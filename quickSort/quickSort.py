# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def quickSort(start,end,arr):
    if end-start <=0:
        return
    pivot = arr[start]
    write = start+1
    for read in range(start+1,end+1):
        if arr[read] <= pivot:
            arr[read],arr[write] = arr[write],arr[read]
            write +=1
    arr[write-1],arr[start] = arr[start],arr[write-1]
    quickSort(start,write-2,arr)
    quickSort(write,end,arr)
    return arr
arr = [3,0,2,-5,10,2]
print(quickSort(0,len(arr)-1,arr))

