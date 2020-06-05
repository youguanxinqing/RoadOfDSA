/*
 * @lc app=leetcode.cn id=27 lang=rust
 *
 * [27] 移除元素
 */

// @lc code=start
impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let l: usize = nums.len(); 
        let mut count: usize = 0;
        for i in 0..l {
            if nums[i] == val {
                count = count + 1;
            } else if i != i-count {
                nums[i-count] = nums[i]
            }
        }
        (l - count) as i32
    }
}
// @lc code=end
