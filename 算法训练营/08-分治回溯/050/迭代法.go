/*
 * @lc app=leetcode.cn id=50 lang=golang
 *
 * [50] Pow(x, n)
 */

// @lc code=start
func myPow(x float64, n int) float64 {
	switch {
	case x == 0:
		return 0
	case n == 0:
		return 1;
	}
	
	// 取正数
	pN := n
	if n < 0 {
		pN = -pN
	} 

	total := 1.0
	for pN > 0 {
		if pN % 2 == 1 {
			total *= x
		}
		pN >>= 1
		x *= x
	}

	if n > 0 {
		return total
	} else { 
		return 1 / total
	}
}
// @lc code=end