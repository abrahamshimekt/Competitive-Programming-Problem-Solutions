def freqAlphabets(self, s: str) -> str:
        i,j=0,1
        letters = []
        prev_j = ""
        while j < len(s):
            if s[j] !='#':
                j +=1
                if j==len(s):
                    prev_j = s[i:j]
            else:
                x = s[i:j]
                if len(x) >2:
                    letters += list(x[:-2])
                    letters.append(x[-2:])
                else:
                    letters.append(s[i:j])
                j +=1
                i =j
        letters += list(prev_j)   
        ans = ''
        for l in letters:
            ans += chr(96+int(l))
        return ans