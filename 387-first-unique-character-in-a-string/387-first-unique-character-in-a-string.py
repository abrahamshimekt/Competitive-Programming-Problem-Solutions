class Solution:
    def firstUniqChar(self, s: str) -> int:
        # first count the the elements of the string using dictionary and find an element in the dictionary that has count of 1 and search its index in the list and return it if not founf return -1
        dic = {}
        dic2 = {}
        n = len(s)
        for i in range(n):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] +=1
        for i in range(n):
            if s[i] not in dic2:
                dic2[s[i]] = i
        for key in dic:
            if dic[key] == 1:
                return dic2[key]
        return -1
                
                
    