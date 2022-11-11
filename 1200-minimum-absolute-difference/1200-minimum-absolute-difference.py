class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minAbsDiff = float("inf")
        arr.sort()
        n = len(arr)
        output = []
        for i in range(n-1):
            minAbsDiff = min(minAbsDiff,arr[i+1]-arr[i])
        for j in range(n-1):
            if arr[j+1]-arr[j] == minAbsDiff:
                output.append([arr[j],arr[j+1]])
        return output
        
            
            