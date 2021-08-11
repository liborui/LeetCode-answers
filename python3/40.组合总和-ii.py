#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
def backtrack(res, path, target, sumNow, cand, start, end):
    if (sum(path) == target):
        if sorted(path[:]) not in res:
            res.append(sorted(path[:]))
            return
    for i in range(start, end):
        # 优化：用于过滤[1, 1, 1, 1, 1, ....]的情况，不要让每次遍历树叶的时候都把所有的重复数据都当做叶子结点再遍历一遍
        if i > start and cand[i] == cand[i-1]:
            continue
        sumNow += cand[i]
        # 优化：用于过滤加上本次选择这个数字之后就超过target的情况
        if sumNow <= target:
            path.append(cand[i])
            # print(path)
            backtrack(res, path, target, sumNow, cand, i+1, end)
            path.pop()
            sumNow -= cand[i]
        else:
            return

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []
        if sum(candidates) == target:
            return [candidates]
        newCandidates = sorted(candidates)
        availCt = len(newCandidates)
        # 优化：直接剔除比target大的数字，他们肯定不会出现在答案中
        for i in range(len(newCandidates)):
            if newCandidates[i] > target:
                availCt = i
                break
        result = []
        path = []
        backtrack(result, path, target, 0, newCandidates, 0, availCt)
        return result
# @lc code=end

