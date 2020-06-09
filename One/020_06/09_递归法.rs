/// 面试题46. 把数字翻译成字符串

/// 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
/// 一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

/// 示例 1:
/// 输入: 12258
/// 输出: 5
/// 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

/// 提示：
/// 0 <= num < 231


impl Solution {
    pub fn translate_num(num: i32) -> i32 {
        let mut res = 0i32;
        Solution::helper(num.to_string().as_str(), &mut res);
        res
    }

    pub fn helper(s: &str, res: &mut i32) {
        if s.len() == 0 {
            *res += 1;
        }

        for i in 1..3 {
            if s.len() >= i && s[..i].to_string().parse::<i32>().unwrap() < 26 {
                if i == 2 && &s[..1] == "0" {
                    continue;
                } else {
                    Solution::helper(&s[i..], res);
                }
            }
        }
    }
}