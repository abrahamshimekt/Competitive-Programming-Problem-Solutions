class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = []
        dic = {}
        arranged = []
    
        for string in strs :
            string = "".join(sorted(string))
            arranged.append(string)
            
        for i in range(len(arranged)):
            if arranged[i] in dic:
                dic[arranged[i]].append(strs[i])
            else:
                dic[arranged[i]] = [strs[i]]

        for key in dic:
            grouped.append(dic[key])
        return grouped
                
       