#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
def checkValidStr(str_long, str_short):
    # if len(str_long) < len(str_short):
    #     return False
    # lst_short = list(str_short)
    # lst_long = list(str_long)
    # for item in lst_short:
    #     if item in lst_long:
    #         lst_long.remove(item)
    #     else:
    #         return False
    # return True

    if len(str_long) < len(str_short):
        return False
    counter_long = Counter(str_long)
    counter_short = Counter(str_short)
    # for item in str_short:
    #     if counter_long[item] < counter_short[item]:
    #         return False
    for k, v in counter_short.items():
        if counter_long[k] < counter_short[k]:
            return False
    return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res_substr = s+"itsjustatest"
        slowIndex, fastIndex = 0, 0
        found = 0
        temp_len = float("INF")
        temp_start = 0
        temp_end = 0
        for fastIndex in range(len(s)):
            temp_substr = s[slowIndex:fastIndex+1]
            # valid = False
            while checkValidStr(temp_substr, t):
                found = 1
                if len(res_substr) > len(temp_substr):
                    res_substr = temp_substr
                # if temp_len > fastIndex-slowIndex+1:
                #     temp_end = fastIndex+1
                #     temp_start = slowIndex
                #     temp_len = fastIndex-slowIndex+1
                slowIndex += 1
                temp_substr = s[slowIndex:fastIndex+1]
        if found == 1:
            # return s[temp_start, temp_end]
            return res_substr
        else:
            return ""
# @lc code=end

