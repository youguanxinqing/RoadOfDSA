/*
 * @lc app=leetcode.cn id=9 lang=rust
 *
 * [9] 回文数
 */

// @lc code=start
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }

        let s = x.to_string();
        let bs = s.as_bytes();
        let (mut l, mut r): (usize, usize) = (0, bs.len()-1);
        while l < r {
            if bs[l] != bs[r] {
                return false;
            }
            l += 1;
            r -= 1;
        }
        return true;
    }
}
// @lc code=end
