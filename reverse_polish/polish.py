class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for index in range(len(tokens)):
            if stack and tokens[index] == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1+num2)
            elif stack and tokens[index] == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2-num1)
            elif stack and tokens[index] == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num1*num2)
            elif stack and tokens[index] == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                if abs(num1) > abs(num2):
                    stack.append(0)
                elif num1 < 0 and num2 > 0:
                    stack.append(-1*(num2//(-1*num1)))
                elif num1 >0 and num2 < 0:
                    stack.append(-1*((-1*num2)//num1))
                else:
                    stack.append(num2//num1)
            else:
                stack.append(int(tokens[index]))
        return stack[0]
        