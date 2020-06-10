/*
 * @lc app=leetcode.cn id=242 lang=golang
 *
 * [242] 有效的字母异位词
 */

// @lc code=start
func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}
	
	m := make(map[byte]int32)
	for i := 0; i<len(s); i++ {
		m[s[i]] += 1
		m[t[i]] -= 1
	}

	for _, v := range m {
		if v != 0 {
			return false
		}
	}
	return true
}
// @lc code=end
