def targetIndices(self, nums: List[int], target: int) -> List[int]:

        max_num = max(nums)
        counting_arr = [0]*(max_num+1)

        for num in  nums:
            counting_arr[num] +=1

        sorted_num = []

        for index in range(max_num+1):
            if counting_arr[index] != 0:
                for count in range(counting_arr[index]):
                    sorted_num.append(index)
        indices = []
        for index_ in range(len(nums)):
            if sorted_num[index_] == target:
                indices.append(index_)
        return indices