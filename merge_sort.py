def merge(left, right):
    arr = []
    while left and right:
        if left[0] > right[0]:
            arr.append(right[0])
            right.pop(0)
        else:
            arr.append(left[0])
            left.pop(0)
    while left:
        arr.append(left[0])
        left.pop(0)
    while right:
        arr.append(right[0])
        right.pop(0)
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:len(arr)]
    l = merge_sort(left)
    r = merge_sort(right)
    return merge(l, r)
