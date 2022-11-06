class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_list = s1.split()
        s2_list = s2.split()
        s1_hashmap = Counter(s1_list)
        s2_hashmap = Counter(s2_list)
        output = []
        for word in s1_hashmap :
            if word not in s2_hashmap and s1_hashmap[word]==1 :
                output.append(word)
        for word in s2_hashmap :
            if word not in s1_hashmap and s2_hashmap[word]==1:
                output.append(word)
        return output
        