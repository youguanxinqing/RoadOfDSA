/*
 * @lc app=leetcode.cn id=22 lang=golang
 *
 * [22] 括号生成
 */

// @lc code=start
func generateParenthesis(n int) []string {
	res := make([]string, 0)
	helper("", n, n, &res)
	return res
}

func helper(s string ,lP, rP int, res *[]string) {
	if rP == 0  {
		*res = append(*res, s)
		return
	}

	if lP == rP { // 相等的时候，要求必须先出 ‘(’
		helper(s+"(", lP-1, rP, res)
	} else if lP < rP {
		if lP > 0 {
			helper(s+"(", lP-1, rP, res)
		}
		helper(s+")", lP, rP-1, res)
	}
}
// @lc code=end