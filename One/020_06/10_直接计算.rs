/*
 * @lc app=leetcode.cn id=9 lang=rust
 *
 * [9] 回文数
 */

// @lc code=start
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 || (x % 10 == 0 && x != 0)  {
            return false;
        }

        let (mut a, mut b): (i32, i32) = (0, x);
        loop {
            a = a * 10 + b % 10;
            if a >= b {
                break;
            }
            
            b /= 10;
            if a >= b {
                break;
            }
        }
        a == b
    }
}
// @lc code=end