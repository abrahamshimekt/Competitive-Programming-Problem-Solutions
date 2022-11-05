class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalks = sum(chalk)
        rem = k% total_chalks
        n = len(chalk)
        for i in range(n):
            if rem > 0:
                rem -= chalk[i]
                if i == n-1:
                    return i 
            elif rem == 0:
                return i
            else:
                return i-1
                