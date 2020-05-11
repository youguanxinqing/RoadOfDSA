/*
 * @lc app=leetcode.cn id=8 lang=golang
 *
 * [8] 字符串转换整数 (atoi)
 */

// @lc code=start
func myAtoi(str string) int {
	const INT32_MAX int32 = int32(^uint32(0) >> 1)
	const INT32_MIN int32 = ^INT32_MAX

	isLess0 := false
	start := 0
	for i, ch := range str {
		switch {
		case ch == ' ':
			continue
		case ch == '-' || ch == '+':
			if ch == '-' {
				isLess0 = true
			}
			start = i+1
			goto block
		case ch >= '0' && ch <= '9':
			start = i
			goto block
		default:
			return 0
		}
	}

block:
	var res int32 = 0
	for i := start; i < len(str) && str[i] >= '0' && str[i] <= '9'; i++ {
		digit := int32(str[i] - '0')
		if res > ( INT32_MAX - digit ) / 10 {
			if !isLess0 {
				return int(INT32_MAX)
			} else {
				return int(INT32_MIN)
			}
		}
		res = res * 10 + digit
	}

	if !isLess0 {
		return int(res)
	} else {
		return int(-res)
	}
}
// @lc code=end