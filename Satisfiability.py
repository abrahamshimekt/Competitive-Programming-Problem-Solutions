class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        reps = {}
        sizes = {}
        for equation in equations:
            a,sign, b = equation[0],equation[1:3],equation[-1]
            reps[a] = a
            reps[b] = b
            sizes[a] = 1
            sizes[b] = 1

        def find(variable):
            while variable != reps[variable]:
                variable = reps[variable]
            return variable
        def union(var1,var2):
            rep1 = find(var1)
            rep2 = find(var2)
            if rep1 != rep2:
                if (reps[rep1] < reps[rep2]) :
                    reps[rep1] = rep2
                elif reps[rep2] < reps[rep1] :
                    reps[rep2] = rep1
                else:
                    reps[rep1] = rep2
                    sizes[rep2] +=1
        for equation in equations:
            a,sign, b = equation[0],equation[1:3],equation[-1]
            if sign == "==":
                union(a,b)
            
                
        for equation in equations:
            a,sign, b = equation[0],equation[1:3],equation[-1]
            rep1,rep2 = find(a),find(b)
            if rep1 == rep2 and sign == "!=":
                return False
           
        return True
                 
