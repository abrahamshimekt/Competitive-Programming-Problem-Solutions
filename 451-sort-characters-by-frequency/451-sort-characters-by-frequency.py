from collections import OrderedDict
class Solution:
    def frequencySort(self, s: str) -> str:
        # use dictionary to count the frequency of each character and sort the dictionary in                 # descending order. 
        # iterate throught the dictionary and append the keys in a list then join the list into a 
        # string . finally return the string 
        ans  = ""
        dic_s = {}
        for c in s:
            if c not in dic_s:
                dic_s[c] = 1
            else:
                dic_s[c] +=1
        sorted_dic_s = dict(sorted(dic_s.items(),key = lambda x:x[1],reverse = True))
        for key in  sorted_dic_s:
            ans +=key* sorted_dic_s[key]
        return ans
        