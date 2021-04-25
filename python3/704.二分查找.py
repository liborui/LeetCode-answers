#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start

## 我的写法
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if target not in nums:
#             return -1
#         pointer = len(nums)//2
#         start = 0
#         end = len(nums) - 1
#         if nums[start] == target:
#             return start
#         elif nums[end] == target:
#             return end
#         else:
#             while pointer != start and pointer != end:
#                 if nums[pointer] == target:
#                     return pointer
#                 elif nums[pointer] > target:
#                     end = pointer
#                     pointer = (start + end)//2
#                 elif nums[pointer] < target:
#                     start = pointer
#                     pointer = (start + end)//2

## 别人优化的写法，重点在于区间的选择。这里我们选择左闭右闭，也即[start, end].如果想要选择左闭右开，代码修改见对应注释
## https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.md
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        start = 0
        end = len(nums)-1                   # end = len(nums)
        middle = 0
        while start <= end:                 # start < end
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle+1
            elif nums[middle] > target:
                end = middle-1              # end = middle
# @lc code=end

