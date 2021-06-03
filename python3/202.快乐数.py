#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        res = []
        sum = n
        while sum not in res:
            res.append(sum)
            string_n = str(sum)
            sum = 0
            for item in string_n:
                sum += int(item)**2
            if sum == 1:
                return True
        return False
# @lc code=end

