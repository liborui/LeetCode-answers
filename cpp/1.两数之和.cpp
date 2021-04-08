/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] 两数之和
 */

// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++){
            vector<int>::iterator it = find(nums.begin(), nums.end(), target-nums[i]);
            if (it != nums.end()){
                cout << distance(nums.begin(), it) << endl;
                vector<int> ret = {i, static_cast<int>(distance(nums.begin(), it))};
                return ret;
            }
        }
    }
};
// @lc code=end

