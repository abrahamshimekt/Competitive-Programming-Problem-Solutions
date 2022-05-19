class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic_strs = {}
        for s in strs:
            if "".join(sorted(s)) not in dic_strs:
                dic_strs["".join(sorted(s))] = [s]
            else:
                dic_strs["".join(sorted(s))].append(s)
        output = []
        for key in dic_strs:
            output.append(dic_strs[key])
        return output
                
       