/*
 * @lc app=leetcode.cn id=11 lang=golang
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
func maxArea(height []int) int {
	max := 0
	l, r := 0, len(height)-1
	length := 0
	for l < r {
		// 选择最短的
		if height[l] < height[r] {
			length = height[l]
		} else {
			length = height[r]
		}
		// 计算面积
		area := (r - l) * length
		
		if max < area {
			max = area
		}
		// 移动指针
		if height[l] < height[r] {
			l++
		} else {
			r--
		}
	}
	return max
}
// @lc code=end