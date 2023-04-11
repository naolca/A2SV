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
        total=0
        d=defaultdict(list)
        for i in range(len(employees)):
            d[employees[i].id]=employees[i]
        def dfs(id):
            nonlocal total
            total+=d[id].importance
            for subordinate in d[id].subordinates:
                dfs(subordinate)
        dfs(id)
        return total