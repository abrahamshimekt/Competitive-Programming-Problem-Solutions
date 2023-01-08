 def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        rearranged = []
        lenght = len(nums)
        # first append the left of the pivot
        # all less than the pivot
        for left in range(lenght):
            if  nums[left] < pivot:
                rearranged.append(nums[left])
            else:
                continue

        # next elements equal to the pivot
        for equal in range(lenght):
            if  nums[equal] == pivot:
                rearranged.append(nums[equal])
            else:
                continue
            
        # finally elements greater than the pivot
        for right in range(lenght):
            if nums[right] > pivot:
                rearranged.append(nums[right])
            else:
                continue


        return rearranged 