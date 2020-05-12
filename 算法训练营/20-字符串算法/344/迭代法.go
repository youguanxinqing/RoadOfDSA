/*
 * @lc app=leetcode.cn id=344 lang=golang
 *
 * [344] 反转字符串
 */

// @lc code=start
func reverseString(s []byte)  {
	mid := len(s) / 2
	num := len(s) - 1
	for i := 0; i < mid; i++ {
		s[i], s[num-i] = s[num-i], s[i]
	}
}
// @lc code=end
