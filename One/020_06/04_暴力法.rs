/*
 * @lc app=leetcode.cn id=238 lang=rust
 *
 * [238] 除自身以外数组的乘积
 */

// @lc code=start
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let l = nums.len();
        let mut rets = vec![0 as i32; l];
        let mut ret: i32 = 1;
        for i in 0..l {
            ret = 1;
            for j in 1..l {
                let idx = (i+j)%l;
                ret = ret * nums[idx];
            }
            rets[i] = ret;
        }
        return rets;
    }
}
// @lc code=end
