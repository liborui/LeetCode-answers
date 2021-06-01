#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0 for i in range(26)]
        for item in s:
            count[ord(item)-ord('a')] += 1
        for item in t:
            count[ord(item)-ord('a')] -= 1
        if count != [0 for i in range(26)]:
            return False
        else:
            return True
# @lc code=end

