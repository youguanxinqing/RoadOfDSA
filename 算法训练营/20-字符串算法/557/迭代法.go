/*
 * @lc app=leetcode.cn id=557 lang=golang
 *
 * [557] 反转字符串中的单词 III
 */

// @lc code=start
func reverseWords(s string) string {
	bytes := []byte(s)
	start := 0
	for i, num := range bytes {
		if num == ' ' {
			reverse(bytes[start:i])
			start = i + 1
		}
	}
	// 收尾
	if start < len(s) {
		reverse(bytes[start:])
	}
	return string(bytes)
}

func reverse(bytes []byte) {
	mid := len(bytes) / 2
	num := len(bytes) - 1
	for i:=0; i < mid; i++ {
		bytes[i], bytes[num - i] = bytes[num - i], bytes[i]
	}
}
// @lc code=end