from collections import Counter
def maxOperations(nums,k):
        counter = Counter(nums)
        output = 0
        for x in counter:
            if counter[k-x] != 0:
                if x != k-x:
                    output += min(counter[x],counter[k-x])
                    counter[x] = 0
                    counter[k-x] =0
                else:
                    output += counter[x]//2
        return output