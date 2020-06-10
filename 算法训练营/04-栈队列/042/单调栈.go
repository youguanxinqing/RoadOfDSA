/*
 * @lc app=leetcode.cn id=42 lang=golang
 *
 * [42] 接雨水
 */

// @lc code=start
func trap(height []int) int {
	h, area := 0, 0
	stack := make([]int, 0)
	for i, curH := range height {
		for len(stack) > 0 && height[stack[len(stack)-1]] < curH {
			idx := stack[len(stack)-1]
			stack = stack[:len(stack)-1] // pop
			if len(stack) == 0 {
				break
			}
			
			// get hegiht
			if height[stack[len(stack)-1]] < curH {
				h = height[stack[len(stack)-1]]
			} else {
				h = curH
			}
			area += (h - height[idx]) * (i - stack[len(stack)-1] - 1)
		}
		stack = append(stack, i)
	}
	return area
}
// @lc code=end