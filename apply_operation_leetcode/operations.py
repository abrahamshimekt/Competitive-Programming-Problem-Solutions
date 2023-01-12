def applyOperations(self, nums: List[int]) -> List[int]:
        length = len(nums)-1
        
        for index in range(length):
            if nums[index] == nums[index+1]:
                nums[index] = nums[index]*2
                nums[index+1] = 0
        
        array = []
        for num in nums:
            if num != 0:
                array.append(num)
        for num_ in nums:
            if num_ == 0:
                array.append(num_)
        return array