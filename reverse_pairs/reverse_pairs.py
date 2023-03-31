class Solution:
    def merge(self,left_half,right_half):
        merged = []
        left = 0
        right = 0
        while left < len(left_half) and right < len(right_half):
            if left_half[left] >= right_half[right]:
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
        if len(nums) ==1:
            return nums
        left_half = self.mergeSort(nums[:len(nums)//2])
        right_half =self.mergeSort(nums[len(nums)//2:])
        
        left = 0
        right = 0
        for left in range(len(left_half)):
            while right < len(right_half) and left_half[left] <= 2*right_half[right]:
                right +=1
            self.reverse_pairs += len(right_half)-right
        return self.merge(left_half,right_half)
            



    def reversePairs(self, nums: List[int]) -> int:
        self.reverse_pairs = 0
        self.mergeSort(nums)
        return self.reverse_pairs

