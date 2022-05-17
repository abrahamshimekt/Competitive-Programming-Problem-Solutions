class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) % 2 == 0 or len(nums) == 1:
            return True

        head_of= [0] * len(nums);
        for i in range(len(nums)-1,-1,-1):
            head_of[i] = nums[i]
            for j in range(i+1, len(nums)):
                head_of[j] = max(nums[i] - head_of[j], nums[j] - head_of[j - 1])
        return head_of[-1] >= 0
                