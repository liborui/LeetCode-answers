#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
def findNextCandidate(target:int, listCandidates: List[int], currentAnswer: List[int], finalAnswer: List[int]):
    for item in listCandidates:
        if target == 0:#(target-item) in listCandidates:
            # currentAnswer.append(item)
            finalAnswer.append(currentAnswer.copy())
            return
        elif target - item < 0:#(target-item) < min(listCandidates):
            currentAnswer = []
            return
        else: #target > min(listCandidates):
            currentAnswer.append(item)
            findNextCandidate(target-item, listCandidates, currentAnswer, finalAnswer)
            currentAnswer.pop()

def delRepeat(finalAnswer: List[int]):
    for item in finalAnswer:
        item.sort()
    tempAnswer = []
    for item in finalAnswer:
        if item not in tempAnswer:
            tempAnswer.append(item)
    return tempAnswer
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []:
            return []
        candidates.sort()
        currentAnswer = []
        finalAnswer = []
        findNextCandidate(target, candidates, currentAnswer, finalAnswer)
        finalAnswer = delRepeat(finalAnswer)
        return finalAnswer
# @lc code=end

