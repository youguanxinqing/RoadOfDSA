/*
 * @lc app=leetcode.cn id=70 lang=golang
 *
 * [70] 爬楼梯
 */

// @lc code=start
func climbStairs(n int) int {
	records := make(map[int]int)
	return helper(n, records)
}

func helper(n int, records map[int]int) int {
	if n < 0 {
		return 0
	} else if n <= 3 {
		return n
	}

	ret, ok := records[n]
	if ok {
		return ret
	}
	ret = helper(n-1, records) + helper(n-2, records)
	records[n] = ret
	return ret
}
// @lc code=end