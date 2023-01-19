def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        mid = 0
        while mid <= right:
            # if the color is zero move it to the left 
            if nums[mid] == 0:
                nums[mid] , nums[left] = nums[left],nums[mid]
                left +=1
                mid += 1
            # if the color is two move it to the right
            elif nums[mid] == 2:
                nums[mid],nums[right] = nums[right],nums[mid]
                right -=1
            # if the color is one do nothing because we want 1 to in the middle 
            # so we don't need to move it the right or to left
            else:
                mid +=1
        return nums