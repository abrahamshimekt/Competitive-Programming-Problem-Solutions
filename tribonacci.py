class Solution:
    def tribonacci(self, n: int) -> int:
        if n== 0:
            return 0
        if n== 1:
            return 1
        if n == 2:
            return 1
        nums = [0,1,1]
        for i in range(n-2):
            nums.append(nums[-1] + nums[-2] + nums[-3])
        return nums[-1]
        
