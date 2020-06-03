/*
 * @lc app=leetcode.cn id=84 lang=golang
 *
 * [84] 柱状图中最大的矩形
 */

// @lc code=start
func largestRectangleArea(heights []int) int {
	length := len(heights) // 数组长度
	var w, j int
	maxArea, area := 0, 0
	for i:=0; i < length; i++ {
		w, j = 0, i
		for j >= 0 && heights[j] >= heights[i] {
			w++
			j--
		}
		j = i + 1
		for j < length && heights[j] >= heights[i] {
			w++
			j++
		}
		area = w * heights[i]
		if area > maxArea {
			maxArea = area
		}
	}
	return maxArea
}
// @lc code=end