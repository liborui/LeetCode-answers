#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## 我的错误解法：[left, right)
        # left = 0
        # right = len(nums)
        # middle = 0
        # if target in nums:
        #     while left < right:
        #         middle = (left + right) // 2
        #         if nums[middle] == target:
        #             return middle
        #         elif nums[middle] < target:
        #             left = middle + 1
        #         elif nums[middle] > target:
        #             right = middle
        # else:
        #     if target > nums[-1]:
        #         return len(nums)
        #     elif target < nums[0]:
        #         return 0
        #     else:
        #         while left < right and middle <= len(nums)-2:
        #             middle = (left + right) // 2
        #             if nums[middle] < target and nums[middle+1] > target:
        #                 return middle + 1
        #             elif nums[middle] < target:
        #                 left = middle + 1
        #             elif nums[middle] > target:
        #                 right = middle

        ## 我的通过解法：[left, right]，64.55% time、23.33% memory，不稳定
        left = 0
        right = len(nums)-1
        middle = 0
        if target in nums:
            while left <= right:
                middle = (left + right) // 2
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    left = middle + 1
                elif nums[middle] > target:
                    right = middle - 1
        else:
            if target > nums[-1]:
                return len(nums)
            elif target < nums[0]:
                return 0
            else:
                while left <= right and middle+1 <= len(nums)-1:
                    middle = (left + right) // 2
                    if nums[middle] < target and nums[middle+1] > target:
                        return middle + 1
                    elif nums[middle] < target:
                        left = middle + 1
                    elif nums[middle] > target:
                        right = middle - 1
        
        ## 他人题解，39.06% time、40.45% memory
        # left = 0
        # right = len(nums)-1
        # middle = 0
        # while left <= right:
        #     middle = left + (right - left) //2      #这样写是为了防止left+right过大，而且这样子写对指针型的left right也有效，之前的加法只适合数值型
        #     if nums[middle] == target:
        #         return middle
        #     elif nums[middle] < target:
        #         left = middle + 1
        #     elif nums[middle] > target:
        #         right = middle - 1
        # return left
# @lc code=end

