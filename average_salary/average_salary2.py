def average(self, salary: List[int]) -> float:
        total = sum(salary)
        min_salary = min(salary)
        max_salary = max(salary)
        return (total-(min_salary+max_salary))/(len(salary)-2)