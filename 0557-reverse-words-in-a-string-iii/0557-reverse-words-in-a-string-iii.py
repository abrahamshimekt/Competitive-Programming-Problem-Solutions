class Solution:
    def reverseWords(self, s: str) -> str:
        strArr = s.split()
        for i in range(len(strArr)):
            strArr[i] = strArr[i][::-1]
        return " ".join(strArr)