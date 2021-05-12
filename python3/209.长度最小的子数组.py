#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 我的解法，超过时限 = =
        # min_length = 0
        # if sum(nums) < target:
        #     return min_length
        # min_length = 100000
        # valid = 1
        # for slowIndex in range(len(nums)):
        #     sum_temp = nums[slowIndex]
        #     fastIndex = slowIndex
        #     while sum_temp < target and fastIndex < len(nums)-1:
        #         fastIndex += 1
        #         sum_temp += nums[fastIndex]
        #         if fastIndex == len(nums)-1 and sum_temp < target:
        #             valid = 0
        #             break
        #     if valid == 0:
        #         break
        #     if sum_temp >= target and min_length > fastIndex-slowIndex+1:
        #         min_length = fastIndex-slowIndex+1
        #     # print(fastIndex, slowIndex, min_length)
        #     slowIndex = fastIndex+1
        # return min_length
        slowIndex, fastIndex = 0, 0
        min_length = float("INF")
        sum_temp = 0
        for fastIndex in range(len(nums)):
            sum_temp += nums[fastIndex]
            while sum_temp >= target:
                min_length = min(fastIndex-slowIndex+1, min_length)
                sum_temp -= nums[slowIndex]
                slowIndex += 1
        if min_length == float("INF"):
            return 0
        else:
            return min_length


# @lc code=end

