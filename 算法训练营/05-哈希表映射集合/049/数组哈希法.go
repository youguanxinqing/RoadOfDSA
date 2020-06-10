/*
 * @lc app=leetcode.cn id=49 lang=golang
 *
 * [49] 字母异位词分组
 */

// @lc code=start
func groupAnagrams(strs []string) [][]string {
	m := make(map[[26]int32][]string)
	
	for _, str := range strs {
		var n [26]int32
		for i := 0; i < len(str); i++ {
			n[str[i] - 'a'] += 1
		}
		m[n] = append(m[n], str)
	}

	res := make([][]string, 0)
	for _, v := range m {
		res = append(res, v)
	}
	return res
}
// @lc code=end