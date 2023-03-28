class Solution:
    def merge(self,left_half,right_half):
        merged = []
        left = 0
        right = 0
        while left < len(left_half) and right < len(right_half):
            if self.nums[left_half[left]] <= self.nums[right_half[right]]:
                
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
    
    def mergeSort(self,left,right):
        if right-left <= 0:
            return [left]
        mid = left + (right-left)//2
        left_half = self.mergeSort(left,mid)
        right_half = self.mergeSort(mid+1,right)
       
       
        for index in range(len(left_half)):
            l = -1
            r = len(right_half)
            while r-l > 1:
                mid = l + (r-l)//2
                
                if self.nums[right_half[mid]] < self.nums[left_half[index]]:
                    l = mid
                else:
                    r = mid
            
            self.answer[left_half[index]] += l+1
              
       
        return self.merge(left_half,right_half)
            


    def countSmaller(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.answer = [0]*len(nums)
        self.mergeSort(0,len(nums)-1)
        return self.answer







