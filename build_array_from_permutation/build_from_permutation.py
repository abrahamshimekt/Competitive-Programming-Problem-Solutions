def buildArray(self, nums: List[int]) -> List[int]:

        length = len(nums)

        # build the array to return the required answer
        answer = [0]*length
        
        for index in range(length):
            answer[index] = nums[nums[index]]
        return answer