class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:

        nums_index = {}
        # store the index of the elements for later retrieval

        for index,num in enumerate(nums):
            nums_index[num] = index
        
        for operation in operations:
            # find the index of the element to be replaced
            replaced_num_index = nums_index[operation[0]]
            # replace the element by operation[i][1]
            nums[replaced_num_index] =operation[1]
            # store the new number with its index
            nums_index[operation[1]] = replaced_num_index
            
        return nums 
