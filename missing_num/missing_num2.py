def missingNumber(self, nums: List[int]) -> int:
        nums_freq = {}
        for num in nums:
            if num not in nums_freq:
                nums_freq[num] =1
            else:
                nums_freq[num] +=1
        n = len(nums)
        for i in range(n+1):
            if i not in nums_freq:
                return i