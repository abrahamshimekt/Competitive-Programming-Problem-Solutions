 def commonChars(self, words: List[str]) -> List[str]:
        freq = [101]*26
        index_found = [0]*26
        length = len(words)

        # check wether a given charcter shown up in all strings
        for word_ in words:
            seen = set()
            for char_ in word_:
                # the set help us to avoid recalculation of occurence of 
                # a character in the given string
                # example for two l's in example 1
                # ls occurrence in bella should be considered once

                if char_ not in seen:
                    index_found[ord(char_)-97] +=1
                    seen.add(char_)

        for word in words:
            # find the frequency of each character in each string
            char_count = Counter(word)
            for char in char_count:
                if index_found[ord(char)-97] == length:
                    freq[ord(char)-97] = min(freq[ord(char)-97],char_count[char])

        common = []
        for index in range(26):
            if freq[index] != 101:
                for count in range(freq[index]):
                    common.append(chr(97+index))
        return common