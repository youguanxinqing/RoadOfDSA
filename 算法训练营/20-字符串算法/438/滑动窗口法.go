/*
 * @lc app=leetcode.cn id=438 lang=golang
 *
 * [438] 找到字符串中所有字母异位词
 */

// @lc code=start
func findAnagrams(s string, p string) []int {
	arr := make([]int, 0)
	if len(p) > len(s) {
		return arr
	}

	var (
		pArr [26]int
		sArr [26]int
		l = 0
		r = 0
	)
	for i := 0; i < len(p); i++ {
		pArr[p[i]-'a']++
		sArr[s[r]-'a']++
		r++
	}
	if pArr == sArr {
		arr = append(arr, l)
	}

	for ; r < len(s); {  // 滑动窗口
		sArr[s[r] - 'a']++
		sArr[s[l] - 'a']--
		r++
		l++
		if sArr == pArr {
			arr = append(arr, l)
		}
	}
	return arr
}

// @lc code=end