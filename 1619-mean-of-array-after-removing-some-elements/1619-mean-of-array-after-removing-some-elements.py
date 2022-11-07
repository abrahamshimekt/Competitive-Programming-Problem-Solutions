class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        min_count = (5*n)//100
        max_count = (5*n)//100
        i = min_count
        total = 0
        while i <=n-max_count-1:
            total += arr[i]
            i +=1
        return total/(n-min_count-max_count)
            