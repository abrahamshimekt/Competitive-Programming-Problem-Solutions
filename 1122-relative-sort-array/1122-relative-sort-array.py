from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []
        arr4 = Counter(arr2)
        i = 0
        while i < len(arr1):
            if arr1[i] not in arr4:
                arr3.append(arr1.pop(i))
            else:
                i +=1
        for num in arr2:
            if num in arr1:
                arr1.remove(num)
        arr3 = sorted(arr3)
        for num in arr1:
            arr2.insert(arr2.index(num),num)
        for num in arr3:
            arr2.append(num)
        return arr2
        