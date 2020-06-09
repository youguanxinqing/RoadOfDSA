/*
 * @lc app=leetcode.cn id=128 lang=rust
 *
 * [128] 最长连续序列
 */

// @lc code=start
impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        if nums.len() < 2 {
            return nums.len() as i32;
        }
        
        use std::collections::HashSet;
        let mut m: HashSet<i32> = HashSet::new();
        for n in nums.iter() { // 去重
            m.insert(*n);
        }

        let mut max = 0i32;
        for v in m.iter() {
            let mut curV = *v;
            let mut count = 1i32;
            while m.contains(&(curV+1)) {
                count += 1;
                curV += 1;
            }
            if count > max {
                max = count;
            }
        }
        max
    }
}
// @lc code=end
