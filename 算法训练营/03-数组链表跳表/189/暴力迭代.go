/*
 * @lc app=leetcode.cn id=189 lang=golang
 *
 * [189] 旋转数组
 */

// @lc code=start
func rotate(nums []int, k int)  {
	length := len(nums)
	for i := 0; i<k; i++ {
		tmp := nums[0]
		for j := 0; j<length; j++ {
			next := j+1
			if next == length {
				next %= length
			}
			tmp, nums[next] = nums[next], tmp
		}
	}
}

// @lc code=end