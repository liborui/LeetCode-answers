#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
def backtrack(res, combineArr, k, start, end):
    if (len(combineArr) == k):
        res.append(combineArr[:])
        return
    for item in range(start, end+1):
        combineArr.append(item)
        backtrack(res, combineArr, k, item+1, end)
        combineArr.pop()

class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        path = []
        backtrack(result, path, k, 1, n)
        return result

# @lc code=end

