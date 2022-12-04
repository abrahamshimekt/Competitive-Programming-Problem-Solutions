class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        n = len(nums)
        for i in range(1,n):
            prefix_sum.append(prefix_sum[i-1] + nums[i])
        index_av_diff = {}
        for j in range(n):
            first = prefix_sum[j]
            last = prefix_sum[-1]-prefix_sum[j]
            if  first >0 and last > 0:
                index_av_diff[j] =  abs(floor(first/(j+1)) - floor(last/(n-j-1)))
            elif first == 0 and last > 0:
                index_av_diff[j] =  abs(floor(last/(n-j-1)))
            elif first >0 and last ==0:
                index_av_diff[j] =  abs(floor(first/(j+1)))
            else:
                index_av_diff[j]  = 0 
        min_average_diff = float('inf')
        for index in index_av_diff:
            if index_av_diff[index] < min_average_diff:
                min_average_diff = index_av_diff[index]
        for indx in index_av_diff:
            if min_average_diff == index_av_diff[indx]:
                return indx
        
            
       
        
        