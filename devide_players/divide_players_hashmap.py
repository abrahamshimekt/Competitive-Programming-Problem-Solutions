from collections import defaultdict
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        length = len(skill)
        min_skill = min(skill)
        max_skill  = max(skill)
        target = min_skill + max_skill
        chemistry = 0
        skills_freq = defaultdict(int)
        team_count = 0
        for sk in skill:
            if skills_freq.get(target-sk,0)>0:
                chemistry += sk*(target-sk)
                team_count +=1
                skills_freq[target-sk] -=1
            else:
                skills_freq[sk] +=1
        return chemistry if team_count == length//2 else -1