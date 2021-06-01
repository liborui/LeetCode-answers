#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # x = set(nums1)
        # y = set(nums2)
        return list(set(nums1)&set(nums2))
# @lc code=end

