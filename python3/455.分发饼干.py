#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gSorted = sorted(g)
        sSorted = sorted(s)
        satisfyCt = 0
        pFound = 0
        finished = False
        for i in range(len(gSorted)):
            for j in range(pFound, len(sSorted)):
                if gSorted[i] <= sSorted[j]:
                    pFound = j + 1
                    satisfyCt += 1
                    print(pFound, gSorted[i], sSorted[j])
                    break

        return satisfyCt
# @lc code=end

