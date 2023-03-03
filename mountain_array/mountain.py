class Solution:
    def isMountainIndex(self,arr,index):
        return arr[index-1] <arr[index] and arr[index]> arr[index+1]
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = -1
        right = len(arr)
        while right - left > 1:
            mid = left + (right-left)//2
            if mid == 0:
                return 1
            elif mid == len(arr)-1:
                return len(arr)-2
            elif self.isMountainIndex(arr,mid):
                return mid
            elif arr[mid-1]<=arr[mid]<=arr[mid+1]:
                left = mid
            else:
                right = mid