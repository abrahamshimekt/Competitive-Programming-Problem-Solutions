class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for c in letters:
            if ord(c) > ord(target):
                return c
        return letters[0]
        