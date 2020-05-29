/*
 * @lc app=leetcode.cn id=26 lang=golang
 *
 * [26] 删除排序数组中的重复项
 */

// @lc code=start
func removeDuplicates(nums []int) int {
	length := len(nums)
	if length < 2 {
		return length
	}
	
	cur, seek := 0, 1
	for ; seek < length; seek++ {
		if nums[cur] == nums[seek] {
			continue
		}
		// 需要交换
		if cur + 1 != seek {
			nums[cur+1] = nums[seek]
		}
		cur++
	}
	return cur+1
}
// @lc code=end