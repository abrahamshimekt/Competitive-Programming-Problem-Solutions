def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        on_right = []
        on_left = []
        equal = []
        lenght = len(nums)

        for index_ in range(lenght):
            # greater than the pivots elements will be added to the right list
            if nums[index_] > pivot:
                on_right.append(nums[index_])
            # less than the pivot elements will be added to the left list 
            elif  nums[index_] < pivot:
                on_left.append(nums[index_])
            # equal too the povit added to the equal list 
            else:
                equal.append(nums[index_])
        
        rearranged = on_left + equal + on_right

        return rearranged 