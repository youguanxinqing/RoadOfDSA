func rotate(nums []int, k int)  {
    length := len(nums)
    k %= length
    for k > 0 {
        saveTail := nums[length-1]
        for i:=length-1; i>0; i-- {
            nums[i] = nums[i-1]
        }
        nums[0] = saveTail
        k--
    }
}
