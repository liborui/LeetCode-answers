#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 1
        result = []
        x, y = 0, 0
        x_limit = len(matrix[0])
        y_limit = len(matrix)
        if len(matrix[0]) == 1:
            direction = 2
        for i in range(x_limit*y_limit):
            result.append(matrix[y][x])
            if direction == 1:
                x += 1
                if x+y == x_limit-1:
                    direction = 2
            elif direction == 2:
                y += 1
                if x-y == x_limit - y_limit:
                    direction = 3
            elif direction == 3:
                x -= 1
                if x+y == y_limit-1:
                    direction = 4
            elif direction == 4:
                y -= 1
                if y-x == 1:
                    direction = 1
        return result
# @lc code=end

