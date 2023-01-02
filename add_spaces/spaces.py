def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces.insert(0,0)
        spaces.append(len(s))
        sentence = ''
        for index in range(len(spaces)-1):
            word = s[spaces[index]:spaces[index+1]]
            if index == 0:
                sentence += f'{word}'
            else:
                 sentence += f' {word}'
        return sentence