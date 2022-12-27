def wrap(string, max_width):
    i = 0
    text = []
    while i < len(string):
        text.append(string[i:i+max_width])
        i +=max_width
    return '\n'.join(text)
        
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)