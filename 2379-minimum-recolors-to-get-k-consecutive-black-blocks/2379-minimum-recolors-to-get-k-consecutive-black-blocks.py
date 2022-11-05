class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0
        flips = float("inf")
        for i in range(k):
            if blocks[i] == "W":
                whites += 1
        j = 1
        flips = min(flips, whites)
        while j + k <= len(blocks):
            if blocks[j - 1] == "W":
                whites -= 1
            if blocks[j + k - 1] == "W":
                whites += 1
            flips = min(flips, whites)
            j += 1
        return flips