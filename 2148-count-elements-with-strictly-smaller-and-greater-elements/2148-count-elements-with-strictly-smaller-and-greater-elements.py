class Solution:
    def countElements(self, nums: List[int]) -> int:
        s_greater = max(nums)
        s_smaller = min(nums)
        count_list = []
        for num in nums:
            if num > s_smaller and num < s_greater:
                count_list.append(num)
        return len(count_list)
        
        