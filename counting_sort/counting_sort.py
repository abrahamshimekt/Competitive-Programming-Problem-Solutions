def countingSort(arr):
    # Write your code here
    freq = [0]*100
    for num in arr:
        freq[num] +=1
    return freq