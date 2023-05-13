class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumB-sumA)//2
        for x in aliceSizes:
            if x + diff in set(bobSizes):
                return [x,x+diff]
        