def validMountainArray(self, arr: List[int]) -> bool:
        pick = 0
        length = len(arr)
        pos = 0
        for index in range(length):
            if arr[index] > pick:
                pick = arr[index]
                pos = index

        if arr[0] == pick or arr[-1] == pick or length <3:
            return False
        elif length == 3 and pos == 1:
            return True
        else:
            left = pos-1
            right = pos+1
            
            while left >0:
                if arr[left] <= arr[left-1]:
                    return False
                left -=1
            while right < length-1:
                if arr[right] <= arr[right+1]:
                    return False
                right +=1
            return True 