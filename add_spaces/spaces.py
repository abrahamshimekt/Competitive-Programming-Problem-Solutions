def addSpaces(self, s: str, spaces: List[int]) -> str:

        # add the starting of the slicing 
        spaces.insert(0,0)
        # add the ending of the slicing
        spaces.append(len(s))

        sentence = ''
        # take two consecutive slicing places 
        # one for starting and one for ending 
        # time complexity is O(N) and O(N) for space 

        for index in range(len(spaces)-1):
            word = s[spaces[index]:spaces[index+1]]
            if index == 0:
                sentence += f'{word}'
            else:
                 sentence += f' {word}'
        return sentence