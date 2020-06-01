/*
 * @lc app=leetcode.cn id=88 lang=golang
 *
 * [88] 合并两个有序数组
 */

// @lc code=start
func merge(nums1 []int, m int, nums2 []int, n int)  {
	for i:=0; i < n; i++ {
		nums1[m+i] = nums2[i]
	}
	sort(nums1, 0, m+n-1)
}

// 快排
func sort(nums1 []int, left, right int) {
	if left >= right {
		return
	}
	 
	i, j := left, right
	for i < j {
		for i < j && nums1[i] <= nums1[j] {
			i++
		}
		nums1[i], nums1[j] = nums1[j], nums1[i]
		for i < j && nums1[j] > nums1[i] {
			j--
		}
		nums1[i], nums1[j] = nums1[j], nums1[i]
	}
	sort(nums1, left, i-1)
	sort(nums1, i+1, right)
}
// @lc code=end