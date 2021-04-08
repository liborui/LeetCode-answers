#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# Version 1: naive
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums:
                if nums.index(temp) != i:
                    return [i, nums.index(temp)]
# @lc code=end

