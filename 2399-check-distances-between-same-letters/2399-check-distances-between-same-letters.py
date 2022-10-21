class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        alphabet = {
                   "a":0,"b":1,"c":2,"d":3,"e":4,"f":5,
                   "g":6,"h":7,"i":8,"j":9,"k":10,"l":11,
                   "m":12,"n":13,"o":14,"p":15,"q":16,"r":17,
                   "s":18,"t":19,"u":20,"v":21,"w":22,"x":23,
                    "y":24,"z":25}
        count = 0
        i= 0
        tracked = {}
        while i < len(s):
            if s[i] not in tracked:
                tracked[s[i]] = 1
                index = alphabet[s[i]]
                move = distance[index]
                if move + 1 + i < len(s) and s[move + 1 + i] == s[i]:
                    i +=1
                else:
                    return False
            else:
                i +=1
        return True
    
                