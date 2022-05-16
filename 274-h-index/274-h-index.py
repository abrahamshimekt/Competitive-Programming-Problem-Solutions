class Solution:
    def hIndex(self, citations: List[int]) -> int:
        dic = {}
        cit_sorted = sorted(citations)
        for i in range(len(cit_sorted)):
            if cit_sorted[i] not in dic:
                dic[cit_sorted[i]] = len(cit_sorted[i:])
        h_index = 0
        print(dic)
        for key in dic:
            if dic[key] >= h_index:
                if dic[key] < key:
                    h_index = dic[key]
                else:
                     h_index = key
        return h_index
            
        