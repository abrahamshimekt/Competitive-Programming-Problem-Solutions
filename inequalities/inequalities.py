class Solution:
    def merge(self,left_half,right_half):
        merged = []
        left = 0
        right = 0
        while left < len(left_half) and right < len(right_half):
            if left_half[left] <= right_half[right]:
                merged.append(left_half[left])
                left +=1
            else:
                merged.append(right_half[right])
                right +=1
        while left < len(left_half):
            merged.append(left_half[left])
            left +=1
        while right < len(right_half):
            merged.append(right_half[right])
            right +=1
        return merged
        

    def mergeSort(self,nums):
        if len(nums)==1:
            return nums
        left_half = self.mergeSort(nums[:len(nums)//2])
        right_half = self.mergeSort(nums[len(nums)//2:])
        ptr = 0
        for index in range(len(left_half)):
            while ptr < len(right_half) and left_half[index]-right_half[ptr] > self.diff:
                ptr +=1
            self.pairs += len(right_half)-ptr
        
        
        return self.merge(left_half,right_half)
        
        

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = []
        self.pairs = 0
        self.diff = diff
        for index in range(len(nums1)):
           nums.append(nums1[index]-nums2[index])
        self.mergeSort(nums)
        return self.pairs
        
        
        