package assign_cookies

import "leetcode/tools/sorts"

func findContentChildren(g, s []int) int {
	sorts.QuickSort(g)
	sorts.QuickSort(s)

	count := 0
	slen := len(s) - 1
	for _, gi := range g {
		if slen < count {
			break
		}
		if gi > s[count] {
			continue
		}
		count++
	}
	return count
}
