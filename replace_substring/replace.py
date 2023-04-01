class Solution:
    def balancedString(self, s: str) -> int:
        N = len(s)
        freq = Counter(s)
        min_length_subarray = float("inf")
        left = 0
        for right in range(len(s)):
            freq[s[right]] -=1
            while left < N and all(N//4 >= freq[char] for char in "WQER"):
                min_length_subarray = min(min_length_subarray,right-left+1)
                freq[s[left]] +=1
                left +=1
        return min_length_subarray



        