/*
 * @lc app=leetcode.cn id=541 lang=golang
 *
 * [541] 反转字符串 II
 */

// @lc code=start
func reverseStr(s string, k int) string {
	str := []byte(s)
	restLen := len(str)
	start := 0
 	for {
		if restLen >= 2 * k { 
			reverse(str[start:start+k])
			start += 2 * k
			restLen -= 2 * k
		} else if restLen > k {  // 2k > restLen > k, 反转前k个，剩余的保持不变
			reverse(str[start:start+k])
			break
		} else {  // restLen < k 全部反转
			reverse(str[start:])
			break
		}
	}
	return string(str)
}

func reverse(str []byte) {
	mid := len(str) / 2 
	num := len(str) - 1
	for i := 0; i < mid; i++ {
		str[i], str[num-i] = str[num-i], str[i]
	}
}
// @lc code=end