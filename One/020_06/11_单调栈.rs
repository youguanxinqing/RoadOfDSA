/*
 * @lc app=leetcode.cn id=739 lang=rust
 *
 * [739] 每日温度
 */

// @lc code=start
impl Solution {
    pub fn daily_temperatures(t: Vec<i32>) -> Vec<i32> {
        let mut res: Vec<i32> = vec![0;t.len()];
        let mut queue: Vec<usize> = vec![];
        for i in 0..t.len() {
            while queue.len() > 0 && t[*queue.last().unwrap()] < t[i] {
                let j = queue.pop().unwrap();
                res[j] = (i - j) as i32;
            }
            queue.push(i);
        }
        res
    }
}
// @lc code=end