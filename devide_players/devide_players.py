class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        length = len(skill)
        teams = length//2
        total_skill = sum(skill)
        if total_skill % teams != 0:
            return -1
        else:
            target = total_skill//teams
            skill.sort()
            left = 0
            right = length -1
            chemistry = 0
            count = 0
            while left < right:
                if skill[left] + skill[right] == target:
                    chemistry += skill[right]*skill[left]
                    count +=1

                left +=1
                right -=1
            return chemistry if count == teams else -1
                