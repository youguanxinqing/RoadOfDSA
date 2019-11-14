func removeDuplicates(nums []int) int {
    if len(nums) == 0 {
        return 0
    }
    mark, flag := 0, nums[0]
    for _, val := range nums {
        if flag != val {
            mark++
            nums[mark], flag = val, val
        }
    }
    return mark + 1
}
