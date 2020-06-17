/*
 * @lc app=leetcode.cn id=1014 lang=rust
 *
 * [1014] 最佳观光组合
 */

// @lc code=start
impl Solution {
    pub fn max_score_sightseeing_pair(a: Vec<i32>) -> i32 {
        if a.len() < 2 {
            return 0i32;
        }
        
        let (mut maxV, mut maxI) = (0i32, a[0]);
        for i in 1..a.len() {
            let v = maxI + a[i] - i as i32;
            if v > maxV {
                maxV = v;
            }

            let i = a[i] + i as i32;
            if i > maxI {
                maxI = i;
            }
        }
        maxV
    }
}
// @lc code=end