def interpret(self, command: str) -> str:
       comnd = list(command)
       ans = ""
       parentheses = {')':"("}
       i =0
       while i < len(comnd)-1:
           if comnd[i] == "(" and comnd[i] == parentheses.get(comnd[i+1],0):
               ans += "o"
               i +=2
           elif comnd[i] == "(" and comnd[i] !=parentheses.get(comnd[i+1],0):
               i +=1
           else:
               if comnd[i] != ")":
                    ans += comnd[i]
               i  +=1
       return ans + command[-1] if command[-1] != ")" else ans
        