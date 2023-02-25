class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = defaultdict(int)
        num_fruits = 0
        left = 0
        curr_count =0
        for right in range(len(fruits)):
            types[fruits[right]] +=1
            curr_count +=1
            while len(types) > 2:
                curr_count -=1
                types[fruits[left]] -=1
                if types[fruits[left]] == 0:
                    del types[fruits[left]]
                left +=1
            num_fruits = max(num_fruits,curr_count)
        return num_fruits



            
            

        