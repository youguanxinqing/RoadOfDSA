/*
 * @lc app=leetcode.cn id=771 lang=golang
 *
 * [771] 宝石与石头
 */

// @lc code=start
func numJewelsInStones(J string, S string) int {
	var arr [256]rune
	for _, ch := range J {
		arr[ch] = 1
	}

	count := 0
	for _, ch := range S {
		if arr[ch] > 0 {
			count++
		}
	}
	return count
}
// @lc code=end
