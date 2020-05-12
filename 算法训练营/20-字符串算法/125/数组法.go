/*
 * @lc app=leetcode.cn id=125 lang=golang
 *
 * [125] 验证回文串
 */

// @lc code=start
func isPalindrome(s string) bool {
	i, j := 0, len(s)-1
	var (
		lArr [36]int
		rArr [36]int
	)
	for ;i < j; i++ {
		if iv := toNum(s[i]); iv != -1 {
			lArr[iv]++
			for ; j >= i; j--{  // 当字符串长度为奇数时，j == i 是必要的
				if jv := toNum(s[j]); jv != -1 {
					rArr[jv]++
					j--
					break
				}
			}
		}

		if lArr != rArr { // 保证过程中总是相等
			return false
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