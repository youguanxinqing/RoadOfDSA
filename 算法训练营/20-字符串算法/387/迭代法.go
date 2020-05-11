/*
 * @lc app=leetcode.cn id=387 lang=golang
 *
 * [387] 字符串中的第一个唯一字符
 */

// @lc code=start
func firstUniqChar(s string) int {
	var arr [256]rune
	for _, i := range s {
		arr[i]++
	}

	for no, i := range s {
		if arr[i] == 1 {
			return no
		}
	}
	return -1
}
// @lc code=end