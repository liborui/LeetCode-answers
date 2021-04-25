#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ## 我的弱智解答
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
        ## 快慢指针法，与暴力解法相比只需要一次for循环
        slowIndex = 0
        for fastIndex in range(len(nums)):
            if nums[fastIndex] != val:
                nums[slowIndex] = nums[fastIndex]
                slowIndex += 1
        return slowIndex

# @lc code=end

