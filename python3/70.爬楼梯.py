#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start

### Version1 backtrack -> out of runtime!
# def backtrace(target: int, steps: List[int], currentRes: List[int], finalRes: List[int]):
#     if target == 0:
#         finalRes.append(currentRes.copy())
#         return
#     for item in steps:
#         if target - item < 0:
#             return
#         else:
#             currentRes.append(item)
#             backtrace(target - item, steps, currentRes, finalRes)
#             currentRes.pop()

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         allowed = [1, 2]
#         currentRes = []
#         finalRes = []
#         backtrace(n, allowed, currentRes, finalRes)
#         return len(finalRes)

### Version2 Fibnacci
### 动态规划思路： 要考虑第爬到第n阶楼梯时候可能是一步，也可能是两步。 
# 1.计算爬上n-1阶楼梯的方法数量。因为再爬1阶就到第n阶 
# 2.计算爬上n-2阶楼梯体方法数量。因为再爬2阶就到第n阶 那么f(n)=f(n-1)+f(n-2);
class Solution:
    def climbStairs(self, n: int) -> int:
        allowed = [0, 1]
        res = []
        if n == 0 or n == 1:
            return n
        res.append(1)
        res.append(2)
        for i in range(1+1, n):
            res.append(res[i-1] + res[i-2])
        return res[n-1]
# @lc code=end

