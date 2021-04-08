#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
def permute(list_a:List[str], list_b:List[str]) -> List[str]:
    res = []
    if len(list_a) == 0:
        res = list_b
    for item_a in list_a:
        for item_b in list_b:
            res.append(item_a+item_b)
    # print(list_a, list_b, res)
    return res

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]
        if digits == "":
            return []
        digits_int = int(digits)
        thousand = digits_int//1000
        handred = (digits_int%1000)//100
        ten = (digits_int%100)//10
        one = digits_int%10
        # print(thousand, handred, ten, one)
        temp = []
        # if thousand == 0 and handred == 0 and ten == 0 and one == 0:
        #     return temp
        # else:
        if thousand != 0:
            temp.append(letters[thousand-2])
        if handred != 0:
            temp.append(letters[handred-2])
        if ten != 0:
            temp.append(letters[ten-2])
        if one != 0:
            temp.append(letters[one-2])
        # print(temp)
        ret = []
        # len_temp = []
        # for item in temp:
        #     len_temp.append(len(item))
        for i in range(len(temp)):
            ret = permute(ret, temp[i])
        return ret
# @lc code=end

