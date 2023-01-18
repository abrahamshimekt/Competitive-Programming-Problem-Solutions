def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = max(arr)
        length = len(arr)
        for index in range(length-1):
            if arr[index] != max_num:
                arr[index] = max_num
            else:
                max_num = max(arr[index+1:])
                arr[index] = max_num
        arr[-1] = -1
        return arr