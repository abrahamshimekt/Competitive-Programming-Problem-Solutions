class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        alphabets = [0]*(len(s)+2)
        for shift in shifts:
            start,end ,step = shift
            if step == 0:
                alphabets[start] -= 1
                alphabets[end + 1] +=1
            else:
                alphabets[start] += 1
                alphabets[end+1] -=1
       
        for index in range(1,len(s)+2):
            alphabets[index] += alphabets[index-1]
        shifted = []
        for indx in range(len(s)):
            asci_val = ord(s[indx])+alphabets[indx]
            if asci_val > 122:
                dist = (asci_val-122)%26
                if dist == 0:
                    shifted.append('z')
                else:
                    shifted.append(chr(dist +96))
            elif asci_val < 97:
                
                dist = (97-asci_val)%26
                if dist == 0:
                    shifted.append("a")
                else:
                    shifted.append(chr(123-dist))
            else:
                shifted.append(chr(asci_val))
        return ''.join(shifted)


        

       

        