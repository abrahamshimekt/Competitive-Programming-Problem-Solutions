class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # loop k times and pop the last element and insert it to 0th place 
        for i in range(k):
            temp = nums.pop()
            nums.insert(0,temp)