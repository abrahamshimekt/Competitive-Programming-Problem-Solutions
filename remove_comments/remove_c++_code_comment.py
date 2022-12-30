def removeComments(self, source: List[str]) -> List[str]:
    
        is_open = False
        code = []
        curr_code = ''

        for line in source:

            index = 0

            # give priority for block comment 
            # if the start of a block comment if found take a flag  true and
            # continue without appending until the flag become false

            while index < len(line):

                if not is_open:
                    if line[index:index+2] == '//':
                        break
                    elif line[index:index+2] =='/*':
                        is_open = True
                        index +=2
                    else:
                        curr_code += line[index]
                        index +=1
                else:
                    if line[index:index+2] == '*/':
                        is_open = False
                        index +=2
                    else:
                        index +=1

            if not is_open:
                code.append(curr_code)
                curr_code = ''
            
        code_without_comment = []

        # remove unnessary empty strings from the list 
        # we only need strings that have a white space 
        
        for lines  in code:
            if lines != '':
                code_without_comment.append(lines)

        return code_without_comment