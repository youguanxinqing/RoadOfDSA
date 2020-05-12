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

	var sArr[26]byte
	var tArr[26]byte
	for i := 0; i < len(s); i++ {
		sArr[s[i]-'a'] += 1
		tArr[t[i]-'a'] += 1
	}

	return sArr == tArr

}
// @lc code=end
