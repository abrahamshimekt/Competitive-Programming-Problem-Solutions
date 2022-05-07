class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use dictionary to check repition 
        # use sliding window 
        # d = {}
        # i = 0
        # j =0
        # maxlenght =0
        # while i < len(s ) and j <len(s):
        #  if s[j] not in d:
        # d[s[j]] = s[j]
        # j +=1
        #   else:
            # maxLength = j-i
            # i +=1
            # remove the elements s[j] from the dic
        if s == " " or len(s) ==1:
            return 1
        else:
            non_repeated ={}
            i = 0
            j = 0
            maxlength =0
            while i < len(s) and j < len(s):
                if s[j] not in non_repeated:
                    if j ==len(s) -1:
                        if maxlength <= j-i:
                             maxlength = j-i+1
                    non_repeated[s[j]] = s[j]
                    j +=1
                else:
                    if maxlength < j -i:
                        maxlength = j -i
                    i +=1
                    non_repeated.pop(list(non_repeated.keys())[0])
            return maxlength
            
