class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q, bank = collections.deque([(start,0)]), set(bank)
        while q:
            g, m = q.popleft()
            if g == end : return m
            for i in range(len(g)):
                for n in "ATGC":
                    gm = g[0:i] + n + g[i+1:]
                    if gm in bank:
                        bank.remove(gm)
                        q.append((gm, m+1))
        
        return -1
