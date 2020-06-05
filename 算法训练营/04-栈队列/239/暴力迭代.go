/*
 * @lc app=leetcode.cn id=239 lang=golang
 *
 * [239] 滑动窗口最大值
 */

// @lc code=start
func maxSlidingWindow(nums []int, k int) []int {
	queue := make([]int, 0, k)
	rets := make([]int, 0)
	var max int
	nums = append(nums, 0) // 填充数
 	for _, v1 := range nums {
		if len(queue) == k {
			// 求最大值
			max = queue[0]
			for _, v2 := range queue[1:] {
				if v2 > max {
					max = v2
				}
			}
			rets = append(rets, max)
			// pop(0)
			queue = queue[1:]
		}
		queue = append(queue, v1)
	}
	return rets
}

// @lc code=end
