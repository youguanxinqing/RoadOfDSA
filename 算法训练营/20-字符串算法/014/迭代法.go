/*
 * @lc app=leetcode.cn id=14 lang=golang
 *
 * [14] 最长公共前缀
 */

// @lc code=start
func longestCommonPrefix(strs []string) string {
	prefix := make([]byte, 0)
	
	if len(strs) < 1 {
		goto block
	}
	
	for i, ch := range strs[0] {
		chByte := byte(ch)
		for _, str := range strs[1:] {
			if i < len(str) && chByte != str[i] {
				goto block
			} else if i >= len(str) {
				goto block
			}
		}
		prefix = append(prefix, chByte)
	}

block:
	return string(prefix)
}
// @lc code=end