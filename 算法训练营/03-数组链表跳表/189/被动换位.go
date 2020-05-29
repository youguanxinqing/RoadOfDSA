/*
 * @lc app=leetcode.cn id=189 lang=golang
 *
 * [189] 旋转数组
 */

// @lc code=start
func rotate(nums []int, k int)  {
	length := len(nums)

	count := 0
	for start:=0; count<length; start++{
		tmp := nums[start]
		next := start
		for {
			next += k
			if next >= length {
				next %= length
			}

			tmp, nums[next] = nums[next], tmp
			count++
			// 回到最初的起点，结束循环
			if next == start {
				break
			}
		}
	}
}
// @lc code=end