func moveZeroes(nums []int)  {
    i := 0
    maxI := len(nums) - 1
    for {
        if i > maxI {
            break
        } else if nums[i] == 0 {
            j := i + 1
            for {
                if j > maxI {
                    break
                } else if nums[j] != 0 {
                    break
                } else {
                    j++
                }
            }

            if j > maxI {
                break
            } else {
                nums[i] = nums[j]
                nums[j] = 0
            }
        }
        i++
    }
}
