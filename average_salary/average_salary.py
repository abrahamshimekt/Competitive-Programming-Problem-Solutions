def average(self, salary: List[int]) -> float:
        total = 0
        min_salary = float('inf')
        max_salary = 0
        for s in salary:
            if s < min_salary:
                min_salary = s
            if s > max_salary:
                max_salary = s
            total += s
        return (total-(min_salary+max_salary))/(len(salary)-2)