class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.insert(0,0)
        arr.append(0)
        min_sum = 0
        stack = []
        mod = 10**9 + 7
        
        for index in range(len(arr)):
            while stack and arr[stack[-1]] > arr[index]:
                mid = stack.pop()
                min_sum += (arr[mid]*(index-mid)*(mid-stack[-1]))%mod
            stack.append(index)
        return min_sum%mod
        