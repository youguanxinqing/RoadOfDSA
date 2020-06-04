/*
 * @lc app=leetcode.cn id=837 lang=rust
 *
 * [837] 新21点
 */

// @lc code=start
impl Solution {
    pub fn new21_game(n: i32, k: i32, w: i32) -> f64 {
        // convert type
        let (n, k, w) = (n as usize, k as usize, w as usize);

        let mut dp = vec![0.0; k+w];
        let mut s = 0.0;
        for i in k..k+w {
            dp[i] = if i <= n {1.0} else {0.0};
            s = s + dp[i];
        }
        for i in (0..k).rev() {
            dp[i] = s / w as f64;
            s = s - dp[i+w] + dp[i];
        }
        dp[0]
    }
}
// @lc code=end