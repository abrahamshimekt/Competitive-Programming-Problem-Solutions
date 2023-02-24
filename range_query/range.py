class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [nums[0]]
        for index in range(1,len(nums)):
            self.prefix_sum.append(self.prefix_sum[index-1] + nums[index])
    def sumRange(self, left: int, right: int) -> int:
        if left !=0:
            return self.prefix_sum[right]-self.prefix_sum[left-1]
        else:
            return self.prefix_sum[right]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)