func merge(nums1 []int, m int, nums2 []int, n int)  {
    j := 0
    for j < n {
        nums1[m] = nums2[j]
        m++
        j++
    }
    sort(nums1, 0, len(nums1)-1)
}

// 快排
func sort(nums []int, left, right int) {
    if left >= right {
        return
    }
    i, j := left, right
    key := nums[i]
    for i < j {
        for i < j && key <= nums[j] {
            j--
        }
        nums[i] = nums[j]
        for i < j && key >= nums[i] {
            i++
        }
        nums[j] = nums[i]
    }
    nums[i] = key
    sort(nums, left, i-1)
    sort(nums, i+1, right)
}
