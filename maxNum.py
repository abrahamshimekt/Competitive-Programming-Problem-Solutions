from ast import List
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        maxNum = 0
        n = len(piles)
        for i in range(n//3,n, 2):
            maxNum += piles[i]
        return maxNum
        # maxNum =0
        # arr1 =[]
        # arr2 =[]
        # for i in range(len(piles)-2):
        #     for j in range( i + 2,len(piles)):
        #         arr1.append(piles[i])
        #         arr1.append(piles[i+1])
        #         arr1.append(piles[j])
        #         arr1.sort()
        #         for num in piles:
        #             if num not in arr1:
        #                 arr2.append(num)
        #         arr2.sort() 
        #         if arr1[-2] + arr2[-2] > maxNum:
        #             maxNum = arr1[-2] + arr2[-2]
        # return maxNum