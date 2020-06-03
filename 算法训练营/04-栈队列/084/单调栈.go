/*
 * @lc app=leetcode.cn id=84 lang=golang
 *
 * [84] 柱状图中最大的矩形
 */

// @lc code=start
func largestRectangleArea(heights []int) int {
	heights = append([]int{0}, append(heights, 0)...)
	var maxArea, area int
	stack := make([]int, 0)
	for i, _ := range heights {
		for len(stack) > 0 && heights[stack[len(stack)-1]] > heights[i] {
			curH := heights[stack[len(stack)-1]]  // 矩形的高
			curW := i - stack[len(stack)-2] - 1
			area = curW * curH
			if area > maxArea {
				maxArea = area
			}
			stack = stack[:len(stack)-1]  // 弹出处理完的元素
		}
		stack = append(stack, i)
	} 
	return maxArea
}
// @lc code=end
