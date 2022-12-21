def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        lossers = {}
        for match in matches:
            if match[0] not in winners:
                winners[match[0]] = 1
            else:
                winners[match[0]] += 1
        for m in matches:
            if m[1] not in lossers:
                lossers[m[1]] = 1
            else:
                lossers[m[1]] += 1
        ans0 = []
        ans1 = []
        for winner in winners:
            if winner not in lossers:
                ans0.append(winner)
        for losser in lossers:
            if lossers[losser] == 1:
                ans1.append(losser)
        ans0 = sorted(ans0)
        ans1 = sorted(ans1)
        return [ans0,ans1]