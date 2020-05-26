/*
 * @lc app=leetcode.cn id=15 lang=golang
 *
 * [15] 三数之和
 */

// @lc code=start
func threeSum(nums []int) [][]int {
	sort.Ints(nums)
	rets := make([][]int, 0)
	
	i := 0
	for i < len(nums)-2 {
		j := i + 1
		k := len(nums) - 1
		for j < k {
			v := nums[i] + nums[j] + nums[k]
			if v == 0 {
				rets = append(rets, []int{
					nums[i], nums[j], nums[k],
				})
				k--
				for j < k && nums[k] == nums[k+1] {
					k--
				}
			} else if v > 0 {
				k--	
				for j < k && nums[k] == nums[k+1] {
					k--
				}
			} else { // v < 0
				j++
				for j < k && nums[j] == nums[j-1] {
					j++
				}
			}
		}

		i++
		for i < len(nums)-2 && nums[i] == nums[i-1] {
			i++
		}
	}
	return rets
}
// @lc code=end