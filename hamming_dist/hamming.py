class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hamming_dist = 0
        while x or y:
            hamming_dist += 1&(x^y)
            x >>=1
            y >>=1
           
        return hamming_dist
