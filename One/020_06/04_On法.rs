/*
 * @lc app=leetcode.cn id=238 lang=rust
 *
 * [238] 除自身以外数组的乘积
 */

// @lc code=start
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let l = nums.len();
        let mut rets = vec![1i32;l];
        let mut m = 1i32;
        for i in 0..l { // 存储左边的数的乘积
            rets[i] = m;
            m = m * nums[i];
        }
        m = 1;
        for i in (0..l).rev() { // 存储右边的数的乘积
            rets[i] = rets[i] * m;
            m = m * nums[i];
        }
        rets
    }
}
// @lc code=end