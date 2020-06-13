/*
 * @lc app=leetcode.cn id=22 lang=golang
 *
 * [22] 括号生成
 */

// @lc code=start
func generateParenthesis(n int) []string {
	switch n {
	case 0:
		return []string{}
	case 1:
		return []string{"()"}
	}

	dp := make([][]string, n+1)
	dp[0], dp[1] = []string{""}, []string{"()"}
	for i:=2; i<=n; i++ {
		for j:=0; j<i; j++ {
			for _, p := range dp[j] {
				for _, q := range dp[i-j-1] {
					s := "(" + p + ")" + q
					dp[i] = append(dp[i], s)
				}
			}
		}
	}
	return dp[n]
}

// @lc code=end