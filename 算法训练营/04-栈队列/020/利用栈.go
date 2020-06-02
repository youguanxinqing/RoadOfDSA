/*
 * @lc app=leetcode.cn id=20 lang=golang
 *
 * [20] 有效的括号
 */

// @lc code=start
func isValid(s string) bool {
	lefts := map[byte]bool{
		'(': true,
		'[': true,
		'{': true,
	}

	stackLen := 0
	stack := make([]byte, stackLen)
	var sentinel byte  // 哨兵
	for i := 0; i<len(s); i++ {
		if lefts[s[i]] {
			stack = append(stack, s[i]) // push
			stackLen++
		} else if len(stack) == 0 {
			return false
		} else {
			switch s[i] {
			case ')': sentinel = '('
			case ']': sentinel = '['
			case '}': sentinel = '{'
			}
			if sentinel == stack[stackLen-1] {
				stackLen--
				stack = stack[:stackLen] // pop
			} else {
				return false
			}
		}
	}

	if len(stack) == 0 {
		return true
	}
	return false
}
// @lc code=end