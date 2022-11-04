class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        j =  1
        n = len(arr)
        max_mountain = 0
        while j < n-1:
            if arr[j] > arr[j-1] and arr[j] > arr[j+1]:
                l= j-1
                r = j +1
                while l >=0 and arr[l] < arr[l+1] :
                    l -=1
                while r < n and arr[r] < arr[r-1]  :
                    r +=1
                max_mountain = max(max_mountain,r-l -1)
                j +=1
            else:
                j +=1
        return max_mountain
                
                
            