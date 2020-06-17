/*
 * @lc app=leetcode.cn id=1014 lang=rust
 *
 * [1014] 最佳观光组合
 */

// @lc code=start
impl Solution {
    pub fn max_score_sightseeing_pair(a: Vec<i32>) -> i32 {
        let mut max = 0i32;
        for i in 0..a.len() {
            for j in i+1..a.len() {
                let tmp: i32 = a[i] + a[j] + i as i32 - j as i32;
                max = if tmp > max { tmp } else { max };
            }
        }
        max
    }
}
// @lc code=end