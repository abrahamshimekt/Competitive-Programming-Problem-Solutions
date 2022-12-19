def swap_case(s):
    modified = ''
    for c in s:
        if ord(c) <97:
            modified +=c.lower()
        else:
            modified += c.upper()
    return modified

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)