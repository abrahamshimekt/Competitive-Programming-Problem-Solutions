
from sortedcontainers import SortedList
class Solution:
    
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = SortedList()
        total_cost =0
        for num in instructions:
        
            less = SortedList.bisect_left(nums,num)
            greater = len(nums)-SortedList.bisect_right(nums,num)

            total_cost += min(less,greater)%(10**9+7)
            nums.add( num)
            
               
        return total_cost%(10**9+7)

            
