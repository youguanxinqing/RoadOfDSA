/*
 * @lc app=leetcode.cn id=1 lang=golang
 *
 * [1] 两数之和
 */

// @lc code=start
func twoSum(nums []int, target int) []int {
	m := make(map[int]int)
    for i, n := range nums {
		m[n] = i
	}

	for i, n := range nums {
		if idx, ok := m[target-n]; ok {
			if i != idx {
				return []int{i, idx}
			}
		}
	}
	return []int{}
}
// @lc code=end
