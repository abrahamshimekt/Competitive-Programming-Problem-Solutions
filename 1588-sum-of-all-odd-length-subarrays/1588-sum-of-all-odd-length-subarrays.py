class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) ==1:
            return arr[0]
        total = sum(arr)
        i = 0
        x = 3
        while i + x <= len(arr):
            total += sum(arr[i:x +i ])
            i +=1
            if x + i > len(arr):
                i = 0
                x +=2
        return total