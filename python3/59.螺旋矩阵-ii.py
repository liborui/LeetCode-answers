#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        matrix = [[0 for x in range(n)] for y in range(n)]
        x = 0
        y = 0
        direction = 1
        for i in range(1, n**2+1):
            matrix[y][x] = i
            if direction == 1:
                x += 1
                if x+y == n-1:
                    direction = 2
            elif direction == 2:
                y += 1
                if x == y:
                    direction = 3
            elif direction == 3:
                x -= 1
                if x+y == n-1:
                    direction = 4
            elif direction == 4:
                y -= 1
                if y-x == 1:
                    direction = 1
        return matrix
# @lc code=end

