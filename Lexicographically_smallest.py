class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        reps = {}
        N = len(s1)
        for index in range(N):

            reps[s1[index]] = s1[index]
            reps[s2[index]] = s2[index]
        def find(char):

            while char != reps.get(char,char):
                char = reps[char]
            return char

        def union(char1,char2):
            rep1 = find(char1)
            rep2 = find(char2)
            if rep1 < rep2:
               reps[rep2] = rep1
            elif rep2 < rep1:
                reps[rep1] = rep2  
        for index in range(N):
            union(s1[index],s2[index])
        answer = []
        for index in range(len(baseStr)):
            answer.append(find(baseStr[index]))
        return "".join(answer)
        
        
        
