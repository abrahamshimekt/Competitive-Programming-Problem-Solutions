class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] =1
            else:
                freq[c] +=1
        freq = sorted(freq.items(),key= lambda x: x[1],reverse= True)
        res = ""
        for item in freq:
            res += item[0]*item[1]
        return res