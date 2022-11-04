class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums) - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] > -1 * nums[i]:
                    right -= 1
                elif nums[left] + nums[right] < -1 * nums[i]:
                    left += 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left - 1] == nums[left] and left < right:
                        left += 1

        return output