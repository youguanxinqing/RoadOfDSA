/*
 * @lc app=leetcode.cn id=283 lang=golang
 *
 * [283] 移动零
 */

// @lc code=start
func moveZeroes(nums []int)  {
	zero := 0 // 0 出现次数
	i := 0
	for ; i < len(nums); i++ {
		if nums[i] == 0 {
			zero++
			continue
		}
		// 不相等就交换
		if i != i-zero {
			nums[i-zero] = nums[i]
		}
	}
	// 末尾归 0
	for i := len(nums); zero > 0; zero-- {
		nums[i-zero] = 0
	}
}
// @lc code=end
