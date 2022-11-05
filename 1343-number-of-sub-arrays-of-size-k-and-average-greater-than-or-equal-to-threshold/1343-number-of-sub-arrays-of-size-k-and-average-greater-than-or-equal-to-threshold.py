class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window_sum = 0
        for i in range(k):
            window_sum += arr[i]
        j = 0
        num_subarray = 0
        while j + k <= len(arr):
            if window_sum/k >= threshold:
                num_subarray +=1
            if j + k == len(arr):
                break
            window_sum -= arr[j]
            window_sum += arr[j+k]
            j +=1
        return num_subarray