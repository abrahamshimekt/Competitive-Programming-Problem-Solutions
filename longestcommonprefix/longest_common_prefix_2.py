class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        if  len(strs[0])==0:
            return ""
        else:
            i , j= 0,0
            temp = strs[0][0]
            ans = ""
            while i < len(strs):
                if strs[i] =="":
                    return ""
                        
                elif j < len(strs[i]):
                    if strs[i][j]==temp:
                        i +=1
                        if i == len(strs):
                            j +=1
                            i = 0
                            ans += temp
                            if j < len(strs[i]):
                                temp = strs[i][j]
                            else:
                                return ans
                    else:
                        return ans
                else:
                    return ans

            
        
        