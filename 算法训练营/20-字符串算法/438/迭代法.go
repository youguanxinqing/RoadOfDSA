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
		sLen = len(s)
		pLen = len(p)
		i = 0 
		j = i+pLen
	)

	pArr := toArr(p)
	for ; j <= sLen; {
		if toArr(s[i:j]) ==  pArr {
			arr = append(arr, i)
		}
		i++
		j++ 
	}
	return arr
}

func toArr(s string) [26]byte {
	var sArr[26]byte
	for i := 0; i < len(s); i++ {
		sArr[s[i]-'a'] += 1
	}
	return sArr
}
// @lc code=end