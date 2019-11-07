func moveZeroes(nums []int)  {
    i, j := 0, 1
    maxJ := len(nums) - 1
    for {
        if j > maxJ {
            break
        } else if nums[i] != 0 {
            i++
            j++
        } else if nums[j] != 0 {
            nums[i] = nums[j]
            nums[j] = 0
            i++
            j++
        } else {
            j++
        }
    }
}
