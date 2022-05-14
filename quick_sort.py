def quick_sort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr.pop()
    pivot_lower = []
    pivot_upper = []
    for item in arr :
        if item > pivot:
            pivot_upper.append(item)
        else:
            pivot_lower.append(item)
    return quick_sort(pivot_lower) + [pivot] + quick_sort(pivot_upper)