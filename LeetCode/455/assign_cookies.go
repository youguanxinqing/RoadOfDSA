package assign_cookies

import "sort"

func findContentChildren(g, s []int) int {
	// 使用官方排序包，用自己的排序函数会导致时间超时
	sort.Ints(g)
	sort.Ints(s)

	count := 0
	glen := len(g) - 1
	for _, si := range s {
		if count > glen {
			break
		}
		// 从最小胃口开始满足(g[0] 最小胃口)
		if si >= g[count] {
			count++
		}
	}
	return count
}
