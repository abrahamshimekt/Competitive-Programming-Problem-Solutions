from ast import List
from operator import add,mul, sub, truediv
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+":add,"-":sub,"*":mul,"/":truediv}
        stack = []
        for token in tokens:
            if token in operators:
                operand1 = stack.pop()
                operand2 = stack.pop()
                stack.append(int(operators[token](operand2,operand1)))
            else:
                stack.append(int(token))
        return stack[0]