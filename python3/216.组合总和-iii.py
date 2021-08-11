#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
def backtrack(path, res, targetSum, targetLen, start, end):
    if (sum(path) == targetSum and len(path) == targetLen):
        res.append(path[:])
        return
    for item in range(start, end+1):
        path.append(item)
        backtrack(path, res, targetSum, targetLen, item+1, end)
        path.pop()

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        path = []
        backtrack(path, result, n, k, 1, 9)
        return result
# @lc code=end

