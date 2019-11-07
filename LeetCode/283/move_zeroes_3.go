func moveZeroes(nums []int)  {
    /* waitZeroIndex 负责等待值为 0 的索引 */
    waitZeroIndex := 0
    for i, val := range nums {
        if val != 0 {
            /* 一旦遇过 0 以后，waitZeroIndex 总是 < i */
            if i > waitZeroIndex {
                nums[waitZeroIndex] = val
                nums[i] = 0
            }
            waitZeroIndex++
        }
    }
}
