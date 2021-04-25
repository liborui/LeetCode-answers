#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_dict = {}
        for i in range(len(cost)):
            cost_dict[i] = cost[i]
        cost_dict = sorted(cost_dict.items(), key=lambda d:d[1])
        print(cost_dict)
# @lc code=end

