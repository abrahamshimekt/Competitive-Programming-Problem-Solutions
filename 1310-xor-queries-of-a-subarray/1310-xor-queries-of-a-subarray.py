class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [arr[0]]
        output = []
        for i in range(1,len(arr)):
            xor.append(xor[i-1]^arr[i])
        for j in range(len(queries)):
            if queries[j][0] == 0:
                output.append(xor[queries[j][1]])
            else:
                output.append(xor[queries[j][0]-1]^xor[queries[j][1]])
        return output
            
           