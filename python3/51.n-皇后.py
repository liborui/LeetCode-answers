#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
def backtrack(res, path, allRows):
    # 按行考虑
    if len(path) == len(allRows):
        res.append(path[:])
        return
    # 按行考虑，每次加一行，就已经考虑了不在一行
    for i in range(len(allRows)):
        # 接下来考虑不能同一列，也就是数字要不一样
        if i not in path:
            # 然后考虑不能是对角线
            ifNoDiag = True
            nowRow = len(path)
            for j in range(len(path)):
                if abs(nowRow - j) == abs(i - path[j]):
                    ifNoDiag = False
                    break
            # 以上三个条件都满足了，才能进入下一层，不然就剪枝
            if ifNoDiag:
                path.append(i)
                backtrack(res, path, allRows)
                path.pop()

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        path = []
        input = []
        for i in range(n):
            input.append(i)
        backtrack(result, path, input)
        # 我们的返回值是[[4, 3, 2, 1], ...]这种样子，要改成题目要求的样子
        returnResult = []
        resStrDict = []
        # 先制作一个返回值的数字和题目要求的字符串的对应关系表
        # 题目说n<=9，所以我用了10个点
        exampleDict = ".........."
        for i in range(n):
            temp = list(exampleDict[:n])
            temp[i] = "Q"
            temp1 = "".join(temp)
            resStrDict.append(temp1)
        # 然后把返回值按照对应关系表替换成题目要求的样子
        for item in result:
            temp = []
            for subitem in item:
                temp.append(resStrDict[subitem])
            returnResult.append(temp)
        return returnResult

# @lc code=end

