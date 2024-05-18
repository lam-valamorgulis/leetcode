#https://leetcode.com/problems/pascals-triangle-ii/


class Solution:

    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1]]
        for i in range(1, rowIndex + 1):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
            row.append(1)
            triangle.append(row)
        return triangle[rowIndex]
