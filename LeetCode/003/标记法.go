/*
 * @lc app=leetcode.cn id=3 lang=rust
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut cs = [-1i32; 128];
        let mut l: i32 = 0;
        let mut max: i32 = 0; 
        for (i, c) in s.as_bytes().iter().enumerate() {
            let idx: usize = *c as usize;
            // >= l, 确保出现的字符不是以前过滤掉
            if cs[idx] >= 0 && cs[idx] >= l {
                if (i as i32 - l + 1) > max {
                    max = i as i32 - l;
                }
                l = cs[idx] + 1;
                cs[idx] = i as i32;
            } else {
                cs[idx] = i as i32;
            }
        }
        
        if s.len() as i32 - l > max {
            max = s.len() as i32 - l;
        }
        max
    }
}
// @lc code=end
