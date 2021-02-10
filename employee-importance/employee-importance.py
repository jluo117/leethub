"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        table = {}
        for employee in employees:
            table[employee.id] = employee
        def helper(employee):
            curImportance = employee.importance
            for sub in employee.subordinates:
                subEmployee = table[sub]
                curImportance += helper(subEmployee)
            return curImportance
        return helper(table[id])
    
        