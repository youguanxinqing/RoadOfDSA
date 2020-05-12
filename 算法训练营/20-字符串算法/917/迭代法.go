/*
 * @lc app=leetcode.cn id=917 lang=golang
 *
 * [917] 仅仅反转字母
 */

// @lc code=start
func reverseOnlyLetters(S string) string {
	bytes := []byte(S)
	start, end := 0, len(S)-1
	for ; start < end; start++ {
		if isAlpah(bytes[start]) { // 如果是字母
			for ;end > start; end-- {
				if isAlpah(bytes[end]) {
					break
				}
			}
			// 交换
			bytes[start], bytes[end] = bytes[end], bytes[start]
			end-- // 交换之后挪位
		}
	}
	return string(bytes)
}

func isAlpah(ch byte) bool {
	return (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')
}
// @lc code=end