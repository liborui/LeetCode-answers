#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowIndex = 0
        for fastIndex in range(len(nums)):
            if nums[fastIndex] != nums[slowIndex]:
                slowIndex += 1
                nums[slowIndex] = nums[fastIndex]
                # print(slowIndex, nums)
        return slowIndex+1
# @lc code=end

