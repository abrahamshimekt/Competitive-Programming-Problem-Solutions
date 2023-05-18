class Solution:
    def isValid(self,s):
        if len(s) == 0 or len(s) > 3 or(len(s) > 1 and s[0] == "0"):
            return False
        num = int(s)
        return num >= 0 and num <= 255
    def backtrack(self,s,pos,currentIp):
        if len(currentIp) == 4 and pos == len(s):
            self.ips.append(".".join(currentIp))
            return 
        for index in range(pos,min(pos+3,len(s))):
            if self.isValid(s[pos:index+1]):
                currentIp.append(s[pos:index+1])
                self.backtrack(s,index + 1,currentIp)
                currentIp.pop()
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ips = []
        self.backtrack(s,0,[])
        return self.ips
        
