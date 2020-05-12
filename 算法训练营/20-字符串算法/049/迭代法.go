/*
 * @lc app=leetcode.cn id=49 lang=golang
 *
 * [49] 字母异位词分组
 */

// @lc code=start
func groupAnagrams(strs []string) [][]string {
	records := make(map[[26]byte]int, 0)
	count := 0

	res := make([][]string, 0)
	for _, str := range strs {
		arr := toArry(str)
		if v, ok := records[arr]; ok {
			res[v] = append(res[v], str)
		} else {
			res = append(res, []string{str})
			records[arr] = count
			count++
		}
	}
	return res
}

func toArry(s string) (arr [26]byte) {
	a := rune('a')
	for _, ch := range s {
		arr[ch - a] += 1
	}
	return
}
// @lc code=end