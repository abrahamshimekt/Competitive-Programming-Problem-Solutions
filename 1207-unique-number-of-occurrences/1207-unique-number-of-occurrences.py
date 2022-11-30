class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts_of_nums = {}
        for num in arr:
            if num not in counts_of_nums:
                counts_of_nums[num] = 1
            else:
                counts_of_nums[num] +=1
        curr_count = 0
        freqs = []
        for number in counts_of_nums:
            freqs.append(counts_of_nums[number])
        freqs.sort()
        curr_freq = 0
        for freq in freqs:
            if freq == curr_freq:
                return False
            curr_freq = freq
        return True
            