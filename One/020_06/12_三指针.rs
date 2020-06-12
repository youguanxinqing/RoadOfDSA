/*
 * @lc app=leetcode.cn id=15 lang=rust
 *
 * [15] 三数之和
 */

// @lc code=start

use std::collections::HashSet;

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();
        
        let mut res: Vec<Vec<i32>> = Vec::new();
        for a in 0..nums.len() {
            // 避开相同元素
            if a > 0 && nums[a] == nums[a-1] {
                continue
            }

            let mut c = nums.len() - 1;
            let target = -nums[a];
            for b in a+1..nums.len() {
                // 避开相同元素
                if b > a + 1 && nums[b] == nums[b - 1] {
                    continue
                }

                while b < c && nums[b] + nums[c] > target {
                    c -= 1; // 左移
                }

                if b == c {
                    break;
                }

                if nums[b] + nums[c] == target {
                    res.push(vec![nums[a], nums[b], nums[c]]);
                }
            }
        }
        res
    }
}
// @lc code=end