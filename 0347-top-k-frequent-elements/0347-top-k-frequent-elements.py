class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result = []
        sorted_freq = sorted(freq.items(),key=lambda x: x[1],reverse = True)
        for num in sorted_freq:
            if k > 0:
                result.append(num[0])
                k -=1
        return result
            