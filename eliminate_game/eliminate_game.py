def findTheDifference(self, s: str, t: str) -> str:
        s_char_freq = Counter(s)
        t_char_freq= Counter(t)
        for char in t_char_freq:
            if char not in s_char_freq:
                return char
            elif t_char_freq[char] > s_char_freq[char]:
                return char