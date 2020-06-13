/*
 * @lc app=leetcode.cn id=70 lang=rust
 *
 * [70] 爬楼梯
 */

// @lc code=start
impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n < 3 {
            return n;
        }

        let n: usize = n as usize;
        let mut arr = vec![0i32; n+1];
        arr[1] = 1;
        arr[2] = 2;
        for i in 3..n+1 {
            arr[i] = arr[i-1] + arr[i-2];
        }
        arr[n]
    }
}
// @lc code=end