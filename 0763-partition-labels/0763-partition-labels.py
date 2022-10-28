class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_appearance = {}
        for i in range(len(s)):
            if s[i] not in last_appearance:
                last_appearance[s[i]] = i
            else:
                last_appearance[s[i]] = i
        output = []
        i=j=0
        max_partition = 0
        while j < len(s):
            max_partition = max(max_partition,last_appearance[s[j]])
            if max_partition == j:
                output.append(j-i +1)
                j +=1
                i = j
                max_partition =0
            else:
                j +=1
        return output