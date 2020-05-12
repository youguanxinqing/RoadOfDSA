/*
 * @lc app=leetcode.cn id=125 lang=golang
 *
 * [125] 验证回文串
 */

// @lc code=start
func isPalindrome(s string) bool {
	i, j := 0, len(s)-1
	for ;i < j; i++ {
		if iv := toNum(s[i]); iv != -1 {
			for ; j >= i; j--{  // 当字符串长度为奇数时，j == i
				if jv := toNum(s[j]); jv != -1 {
					if jv != iv {
						return false
					} else {
						j--
						break
					}
				}
			}
		}
	}
	return true
}

func toNum(ch byte) int {
	switch {
	case ch >= 'a' && ch <= 'z':
		return int(ch - 'a' + 10)
	case ch >= 'A' && ch <= 'Z':
		return int(ch - 'A' + 10)
	case ch >= '0' && ch <= '9':
		return int(ch - '0')
	default: 
		return -1
	}
}
// @lc code=end