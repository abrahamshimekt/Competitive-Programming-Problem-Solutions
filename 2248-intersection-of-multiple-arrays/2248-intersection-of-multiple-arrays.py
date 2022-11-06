class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        nums_count = {}
        output = []
        m = len(nums)
        for arr in nums:
            n = len(arr)
            for i in range(n):
                if arr[i] in nums_count:
                    nums_count[arr[i]] += 1
                else:
                    nums_count[arr[i]] = 1
        for num in arr:
            if nums_count[num] == m:
                output.append(num)
        return sorted(output)
            
            