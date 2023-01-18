def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        max_num = -1
        for index in range(length-1,-1,-1):
            curr_num = arr[index]
            arr[index] = max_num
            max_num = max(curr_num,max_num)
        return arr