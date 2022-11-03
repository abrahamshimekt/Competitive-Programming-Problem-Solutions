class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0
        n = len(chars)
        current_char = chars[0]
        s = ""
        while j <= n:
            if j <=n-1 and current_char == chars[j]:
                s += chars[j]
                j +=1
            else:
                s_len = len(s)
                if s_len == 1:
                    chars[i] = s[0]
                    s = ""
                    i +=1
                    if j < n:
                        current_char = chars[j]
                elif s_len > 1:
                    chars[i] = s[0]
                    s_len = f"{s_len}"
                    for k in range(len(s_len)):
                        chars[i+k + 1] = s_len[k]
                    s = ""
                    i +=len(s_len)+1
                    if j < n:
                        current_char = chars[j]
                else:
                    break
        return i
                        
                
                
                    
            