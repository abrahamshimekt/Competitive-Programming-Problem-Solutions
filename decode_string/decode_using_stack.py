class Solution:
    def decodeString(self, s: str) -> str:
        digit_stack = []
        char_stack = ['']
        index = 0
        while index < len(s):
            
            if s[index] == ']':
                chars = []
                while  char_stack[-1] != '[':
                   chars.append(char_stack.pop())
                char_stack.pop()
                multi = digit_stack.pop()
                chars = multi * "".join(chars)
                for char in chars[::-1]:
                    char_stack.append(char)
                index +=1
            elif s[index].isdigit():
                digit = []
                while index < len(s) and s[index].isdigit():
                    digit.append(s[index])
                    index +=1
                digit_stack.append(int("".join(digit)))
            else:
                char_stack.append(s[index])
                index +=1

        return ''.join(char_stack)




        