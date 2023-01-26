class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        length = len(skill)
        chemistry = 0
        target = skill[0] + skill[-1]

        left = 0
        right = length -1
       
        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            else:
                chemistry += skill[right]*skill[left]
            left +=1
            right -=1
        return chemistry 