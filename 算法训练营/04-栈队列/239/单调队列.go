/*
 * @lc app=leetcode.cn id=239 lang=golang
 *
 * [239] 滑动窗口最大值
 */

// @lc code=start
func maxSlidingWindow(nums []int, k int) []int {
	stack := make([]int, 0, k)
	// 准备数据
	for i, v := range nums[:k] {
		for len(stack) > 0 && nums[stack[len(stack)-1]] <= v {
			stack = stack[:len(stack)-1] //pop(-1)
		}
		stack = append(stack, i)
	}

	rets := make([]int, 0)
	rets = append(rets, nums[stack[0]])
	for i, v := range nums[k:] {
		i += k
		if i-k >= stack[0] {
			// pop(0)
			stack = stack[1:]
		}
		for len(stack)>0 && nums[stack[len(stack)-1]] <= v {
			// pop(-1)
			stack = stack[:len(stack)-1] //pop(-1)
		}
		stack = append(stack, i)
		rets = append(rets, nums[stack[0]])
	}
	return rets
}

// @lc code=end
