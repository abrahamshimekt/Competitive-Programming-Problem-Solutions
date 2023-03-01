class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left =0
        window = defaultdict(int)
        longest_repeating = 0
        for right in range(len(s)):
            window[s[right]]+=1
            max_freq = max(window.values())
        
            while right-left +1 - max_freq > k:
                window[s[left]] -=1
                if window[s[left]] == 0:
                    del window[s[left]]
                left +=1
            longest_repeating = max(longest_repeating,right-left+1)
        return longest_repeating
            

        