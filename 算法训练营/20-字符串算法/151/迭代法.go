/*
 * @lc app=leetcode.cn id=151 lang=golang
 *
 * [151] 翻转字符串里的单词
 */

// @lc code=start
func reverseWords(s string) string {
	bytes := make([]byte, 0)
	num := len(s) - 1
	wordBorder := 0  // 单词结尾
	for ;num >= 0; num-- {
		if s[num] != ' ' {
			if wordBorder == 0 {
				wordBorder = num+1
			}
			continue
		}

		if wordBorder != 0 {
			bytes = append(bytes, ' ')  // 保留空格
			bytes = append(bytes, s[num+1:wordBorder]...)
			wordBorder = 0
		}
	}

	// 收尾
	if wordBorder != 0 {
		bytes = append(bytes, ' ')  // 保留空格
		bytes = append(bytes, s[num+1:wordBorder]...)
	}

	if len(bytes) == 0 {
		return string(bytes)
	} else {
		return string(bytes[1:])
	}
}
// @lc code=end