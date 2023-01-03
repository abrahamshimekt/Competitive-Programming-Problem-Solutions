class Solution:
    def printVertically(self, s: str) -> List[str]:

        max_length = 0
        words = s.split()

        for word in words:
            max_length = max(max_length,len(word))

        grid_words = []

        for word_ in words:
            word_ += ' '* (max_length-len(word_))
            grid_words.append(word_)
        
        # m and n are the rows and columns
        m = len(grid_words)
        n = len(grid_words[0])

        output = []

        for row in range(n):
            new_word = ''
            for col in range(m):
                new_word += grid_words[col][row]
            output.append(new_word.rstrip())
            
        return output




        

        
