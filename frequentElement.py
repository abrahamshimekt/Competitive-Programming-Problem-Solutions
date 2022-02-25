def maxFrequency(self, nums):
        nums.sort()
        left = 0
        right = 1

        while right < len(nums):
            k -= (nums[right] - nums[right-1]) * (right - left)

            if k < 0:
                k += nums[right] - nums[left]
                left += 1

            right += 1

        return right - left