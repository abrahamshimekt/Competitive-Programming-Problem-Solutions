class Solution:
    def compress(self, chars: List[str]) -> int:
     
        slow = fast = 0
        inserter = 0
        count = 0
        length = len(chars)

        while fast <= length:
            if fast < length and chars[slow] == chars[fast]:
                count +=1
                fast +=1
            else:
                if count == 1:
                    chars[inserter] = chars[slow]
                    inserter +=1
                    count = 0
                elif count > 1:
                    chars[inserter] = chars[slow]
                    inserter +=1 
                    count_s = str(count)
                    for s in count_s:
                        chars[inserter] = s
                        inserter +=1 
                    count = 0
                slow = fast
                if fast == length:
                    break
               
        return inserter 



                     



         
        