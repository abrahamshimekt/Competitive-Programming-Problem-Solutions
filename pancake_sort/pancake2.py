class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        target = sorted(arr)
        right = len(arr)
        flips = []
        for index in range(right-1,-1,-1):
            pivot = arr.index(target[index])
            flips.append(pivot+1)
            arr = arr[pivot::-1] + arr[pivot+1:]
            flips.append(index+1)
            arr = arr[index::-1] + arr[index+1:]
        return flips