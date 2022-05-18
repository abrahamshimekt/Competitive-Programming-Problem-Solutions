class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        target = max(arr)
        return arr.index(target)
        # if target==arr[len(arr)//2]:
        #     return len(arr)//2
        # elif arr.index(target) > len(arr)//2:
        #     return self.peakIndexInMountainArray(arr[(len(arr)//2)+1:])
        # else:
        #     return self.peakIndexInMountainArray(arr[(len(arr)//2):])
            
        