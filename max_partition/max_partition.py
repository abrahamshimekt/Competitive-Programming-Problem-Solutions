class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}
        length = len(s)
        for index in range(length):
            last_occurrence[s[index]] = index

        sizes = []
        fast = 0
        slow = 0
        max_partition = 0
        while fast < length:
            max_partition = max(max_partition,last_occurrence[s[fast]])
            if max_partition == fast:
                sizes.append(fast-slow+1)
                slow = fast+1
            fast +=1
        return sizes




        