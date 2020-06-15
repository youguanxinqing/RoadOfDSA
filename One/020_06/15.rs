/*
 * @lc app=leetcode.cn id=14 lang=rust
 *
 * [14] 最长公共前缀
 */

// @lc code=start
impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.len() < 1 {
            return String::from("");
        }

        let mut res = String::new();
        'outer: for i in 0..strs[0].len() {
            let slc = &strs[0][i..i+1];
            for item in strs.clone() {
                if item.len() <= i || &item[i..i+1] != slc {
                    break 'outer;
                }
            }
            res.push_str(slc);
        }
        res
    }
}
// @lc code=end