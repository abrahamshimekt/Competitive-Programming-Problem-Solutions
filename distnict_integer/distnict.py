def countDistinctIntegers(self, nums: List[int]) -> int:
        lenght = len(nums)
        for index in range(lenght):
            num = str(nums[index])
            nums.append(int(num[::-1]))
        unique = set()
        for num_ in nums:
            unique.add(num_)
        return len(unique)