#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap1 = {}
        for item1 in nums1:
            for item2 in nums2:
                if item1+item2 not in hashmap1.keys():
                    hashmap1[item1+item2] = 1
                else:
                    hashmap1[item1+item2] += 1
        hashmap2 = {}
        for item1 in nums3:
            for item2 in nums4:
                if item1+item2 not in hashmap2.keys():
                    hashmap2[item1+item2] = 1
                else:
                    hashmap2[item1+item2] += 1
        result = 0
        for key, value in hashmap1.items():
            if -key in hashmap2.keys():
                result += hashmap2[-key]*hashmap1[key]
        return result

                         
# @lc code=end

