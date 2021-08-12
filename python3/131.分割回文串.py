#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
def backtrack(res, path, oriStr, separatedLen):
    if separatedLen == len(oriStr):
        res.append(path[:])
        return
    for i in range(1, len(oriStr)-separatedLen+1):
        temp = "".join(oriStr[separatedLen : separatedLen+i])
        isCircle = True
        for j in range(len(temp)):
            if temp[j] != temp[len(temp)-1-j]:
                isCircle = False
                break
        if isCircle:
            path.append(temp)
            backtrack(res, path, oriStr, separatedLen+i)
            path.pop()
        else:
            continue

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        input = list(s)
        path = []
        result = []
        backtrack(result, path, input, 0)
        return result

# @lc code=end

