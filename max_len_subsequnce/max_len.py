class Solution:
    def backTrack(self,index,subsequence):
        if index >=self.N:

            if len(set(''.join(subsequence))) == len(''.join(subsequence)):
                self.subsequences.append(subsequence[:])
            return
        subsequence.append(self.arr[index])
        self.backTrack(index+1,subsequence)
        subsequence.pop()
        self.backTrack(index+1,subsequence)

    def maxLength(self, arr: List[str]) -> int:
        self.N = len(arr)
        self.arr = arr
        self.subsequences = []
        self.backTrack(0,[])
        max_len = 0
        for index in range(len(self.subsequences)):
            max_len = max(max_len,len("".join(self.subsequences[index])))
        

        return max_len