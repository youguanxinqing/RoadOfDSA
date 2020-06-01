/*
 * @lc app=leetcode.cn id=66 lang=golang
 *
 * [66] 加一
 */

// @lc code=start
func plusOne(digits []int) []int {
	num := len(digits)-1
	for num >= 0 {
		digits[num] += 1
		if digits[num] < 10 {
			break
		}
		digits[num] %= 10
		num--
	}

	if digits[0] != 0 {
		return digits
	} else {
		new_digits := []int{1}
		new_digits = append(new_digits, digits...)
		return new_digits
	}
}
// @lc code=end