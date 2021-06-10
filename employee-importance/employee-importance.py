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
        def helper(curEmployee: Employee):
            count = curEmployee.importance
            for sub in curEmployee.subordinates:
                count += helper(table[sub])
            return count
        return helper(table[id])
        