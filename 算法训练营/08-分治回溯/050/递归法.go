/*
 * @lc app=leetcode.cn id=50 lang=golang
 *
 * [50] Pow(x, n)
 */

// @lc code=start
func myPow(x float64, n int) float64 {
	switch {
	case x == 0.0:
		return 0.0
	case n == 0:
		return 1.0
	}

	return helper(x, n)
}

func helper(x float64, n int) float64 {
	if n < 0 {
		return helper(1/x, -n)
	} else if n == 0 {
		return 1.0
	}

	if n % 2 == 1 {
		return x * helper(x, n-1)
	}
	return helper(x*x, n>>1)
}
// @lc code=end