package main

import (
	"fmt"
	"sort"
)

func twoSum(nums []int, target int) []int {
	numsBak := make([]int, len(nums))
	copy(numsBak, nums)
	sort.Ints(nums)

	l := 0
	r := len(nums) - 1
	res := []int{}
	for l < r {
		if nums[l]+nums[r] > target {
			r--
		} else if nums[l]+nums[r] < target {
			l++
		} else {
			// 寻找索引
			for i, v := range numsBak {
				// 避免重复元素
				if len(res) != 2 {
					if v == nums[l] {
						res = append(res, i)
					} else if v == nums[r] {
						res = append(res, i)
					}
				} else {
					return res
				}
			}
		}
	}
	return res
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	fmt.Println(twoSum(nums, target))
}
