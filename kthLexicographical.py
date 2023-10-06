class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def getCountNode(n,curr):
            total = 0
            nxt = curr + 1
            while curr<=n:
                total += min(n-curr + 1,nxt-curr)
                curr *=10
                nxt *=10
            return total
        curr = 1
        k -=1
        while k > 0:
            nodes = getCountNode(n,curr)
            if k >= nodes:
                curr +=1
                k-=nodes
            else:
                curr*=10
                k-=1
        return curr
        

        
