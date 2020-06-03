/*
 * @lc app=leetcode.cn id=837 lang=rust
 *
 * [837] 新21点
 */

// @lc code=start
impl Solution {
    pub fn new21_game(n: i32, k: i32, w: i32) -> f64 {
        let mut s: f64 = 0.0;
        let mut dp = vec![0.0; (k+w) as usize];
        for i in k..k+w {
            dp[i as usize] = if i <= n {1 as f64} else {0 as f64};
            s = s + dp[i as usize];
        }
        for i in (0..k).rev() {
            dp[i as usize] = s / (w as f64);
            s = s - dp[(i+w) as usize] + dp[i as usize];
        }
        dp[0]
    }
}
// @lc code=end