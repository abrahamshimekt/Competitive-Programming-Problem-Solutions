class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return

        pivot = random.choice(nums)
        left,mid,right = [],[],[]

        for num in nums:
            if num > pivot:
                left.append(num)
            elif num < pivot:
                right.append(num)
            else:
                mid.append(num)
        L , M = len(left), len(mid)

        if k<= L:
            return self.findKthLargest(left,k)
        
        elif k > L+ M:
            return self.findKthLargest(right, k-L-M)
            
        else:
            return mid[0]
