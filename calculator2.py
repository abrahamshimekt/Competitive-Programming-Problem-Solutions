class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        exp = []
        num =0
        op = "+"
        for i, c in enumerate(s):
            if c.isdigit():
                num = num*10 + int(c)
            if (not c.isdigit() and c != " ") or i == len(s)-1:
                if op =="+":
                    exp.append(num)
                elif op =="-":
                    exp.append(-num)
                elif op == "*":
                    exp.append(exp.pop() * num)
                else:
                    left = exp.pop()
                    exp.append(left //num)
                    if left // num < 0 and left % num !=0:
                        exp[-1] +=1
                num =0
                op = c
        return sum(exp)
                
                    
            
