def isValid(sequence):
    while True:
        if '()' in sequence:
            sequence = sequence.replace('()','')
        elif '()' in sequence:
            sequence = sequence.replace('()','')
        elif '()' in sequence:
            sequence = sequence.replace('()','')
        else:
            return not sequence
def isValid(self, s: str) -> bool:
    stack =[]
    dic ={'(':')','{':'}','[':']'}
    for i in range(len(s)):
        if i ==0 or stack ==[]:
            stack.append(s[i])
        else:
            if dic.get(stack[-1],"o" )== s[i]:
                stack.pop()
            else:
                stack.append(s[i])
    return stack ==[]
