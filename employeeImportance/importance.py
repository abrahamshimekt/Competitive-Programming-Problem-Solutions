"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def findEmployee(self,id):
        for employee in self.employees:
            if employee.id == id:
                return employee

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.employees = employees
        employee = self.findEmployee(id)
        stack = [employee]
        importance = 0
        while stack:
            employee = stack.pop()
           
            importance += employee.importance
            for subordinate in employee.subordinates:
                stack.append(self.findEmployee(subordinate))
        return importance

       

        