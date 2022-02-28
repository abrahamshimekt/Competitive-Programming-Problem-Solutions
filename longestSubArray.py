class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
            maxLength = 0
            maxHeap = []
            minHeap = []
            beg = 0
            end = 0
            while (end < len(nums)):
                currEl = nums[end]
                while (len(maxHeap) > 0 and nums[maxHeap[-1]] <= currEl):
                    del maxHeap[-1]
                maxHeap.append(end)
                while (len(minHeap) > 0 and nums[minHeap[-1]] >= currEl):
                    del minHeap[-1]
                minHeap.append(end)
                maxOfSub = nums[maxHeap[0]]
                minOfSub = nums[minHeap[0]]
                if (maxOfSub - minOfSub <= limit):
                    currLength = end - beg + 1
                    if (maxLength < currLength):
                        maxLength = currLength
                else:
                    beg += 1
                    while (len(minHeap) > 0 and minHeap[0] < beg):
                        del minHeap[0]

                    while (len(maxHeap) > 0 and maxHeap[0] < beg):
                        del maxHeap[0]

                end += 1
            return maxLength
#         maxLen=1
#         maxD=nums[0]
#         minD=nums[0]
#         temp=nums[0:1]
#         for i in range(1,len(nums)):
#             temp.append(nums[i])
#             if nums[i]>maxD:
#                 maxD=nums[i]
#             if nums[i]<minD:
#                 minD=nums[i]
                
#             if maxD-minD<=limit:
#                 if len(temp)>maxLen:
#                     maxLen=len(temp)
#             else:
#                 temp.pop(0)
#                 while  max(temp)-min(temp)>limit:
#                     temp.pop(0)
#                 maxD=max(temp)
#                 minD=min(temp)
      
#         return maxLen;
    
    
        # maxLen = 0
        # arr =[]
        # for i in range(len(nums)):
        #     for j in range(i + 1 , len(nums)):
        #         arr = nums[i:j]
        #         if max(arr) - min(arr) <= limit:
        #             maxLen = max(maxLen,len(arr))
        # return maxLen
        