class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        target = sorted(arr)
        length = len(arr)
        nums_indics = {}

        for pos in range(length):
            nums_indics[arr[pos]] = pos
        flips = []
        for index in range(length-1,-1,-1):
            pivot = nums_indics[target[index]]
            flips.append(pivot+1)

            right = pivot
            left = 0

            while left < right:
                arr[left],arr[right] = arr[right],arr[left]
                nums_indics[arr[left]] = left
                nums_indics[arr[right]] = right
                left +=1
                right -=1

            flips.append(index+1)

            r = index
            l = 0

            while l < r:
                arr[l],arr[r] = arr[r],arr[l]
                nums_indics[arr[l]] = l
                nums_indics[arr[r]] = r
                l +=1
                r -=1

        return flips
