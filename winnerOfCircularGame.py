class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = []
        for i in range(1,n +1):
            nums.append(i)
        current = len(nums) -1
        while len(nums) !=1:
            current = (current + k) % len(nums) 
            nums.remove(nums[current])
            current -=1
            current %= len(nums)
        return nums[0]