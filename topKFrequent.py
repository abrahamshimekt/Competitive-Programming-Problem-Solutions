from collections import Counter
class Solution:
    def topKFrequent(self, nums,k):
        sortedNum= sorted(Counter(nums).items(), key = lambda x:x[1], reverse = True)
        outPut =[]
        for i in range(k):
            outPut.append(sortedNum[i][0])
        return outPut
if __name__=="__main__":
    s = Solution()
    print(s.topKFrequent([2,3,5,6,8,7,7,8,1,3],3))