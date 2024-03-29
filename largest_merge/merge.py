class Solution:
    # if ith character of the two words are equal we need to find that which 
    # word is greater from the current position on wards
    def compare(self,word1,word2,f,s):
        w1,w2 = word1[f:] ,word2[s:]
        if w1 >= w2:
            return True
        else:
            return False
       
    def largestMerge(self, word1: str, word2: str) -> str:
        f = s= 0
        merge = []
        while f < len(word1) or s < len(word2):
            if f < len(word1) and s < len(word2):
                if word1[f] > word2[s]:
                    merge.append(word1[f])
                    f +=1
                elif word2[s] > word1[f]:
                    merge.append(word2[s])
                    s +=1
                else:
                    choice= self.compare(word1,word2,f,s)
                    if choice == True:
                        merge.append(word1[f])
                        f +=1
                    else: 
                        merge.append(word2[s])
                        s +=1
                
            elif f >= len(word1) and s<len(word2):
                merge.append(word2[s:])
                break
            elif s>= len(word2) and f< len(word1):
                merge.append(word1[f:])
                break
        return ''.join(merge)
                    
                
                
                            
                           
                
       


                



                


