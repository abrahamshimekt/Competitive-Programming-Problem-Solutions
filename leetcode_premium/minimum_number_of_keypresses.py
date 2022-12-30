class Solution:
    def count_letters(self,word):
        freq = {}
        for char in word:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] +=1
        freq = dict(sorted(freq.items(),key = lambda x:x[1],reverse=True))
        return freq

    def minimumKeypresses(self, s: str) -> int:

        word_freq = self.count_letters(s)
        keyboard = {}
        index = 1

        for item in word_freq:
            if index > 9:
                index = index%9
            if index not in keyboard:
                keyboard[index] = [item[0]]
            else:
                keyboard[index].append(item[0]) 
            index +=1

        key_press = 0

        for key in keyboard:
            for indxx  in range(len(keyboard[key])):
                key_press += (indxx+1)*word_freq[keyboard[key][indxx]]
                
        return key_press



       


            
        
        

        




