from typing import List

"""
LeetCode: 3531 - Count Covered Buildings
Approach: Track min/max coordinates for each row/column, then count buildings strictly inside both their row and column bounds.
Time: O(n + b) where n is grid size and b is number of buildings; Space: O(n) for row/column bounds.
"""

class Solution:
    def _max(self, value):
        return [0] * (value + 1)
    
    def _min(self, value):
        return [value + 1] * (value + 1)

    def countCoveredBuildings(self, n: int, buildings: List[List[int]]):
        maxRow = self._max(n)
        minRow = self._min(n)
        maxCol = self._max(n)
        minCol = self._min(n)
        
        for position in buildings:
            x = position[0]
            y = position[1]
            maxRow[y] = max(maxRow[y], x)
            minRow[y] = min(minRow[y], x)
            maxCol[x] = max(maxCol[x], y)
            minCol[x] = min(minCol[x], y)
            
        result = 0
        
        for position in buildings:
            x = position[0]
            y = position[1]
            
            if (x > minRow[y] and x < maxRow[y] and y > minCol[x] and y < maxCol[x]):
                result += 1
        
        return result
        
# test
sol = Solution()
print(sol.countCoveredBuildings(3, [[1,2],[2,2],[3,2],[2,1],[2,3]]))