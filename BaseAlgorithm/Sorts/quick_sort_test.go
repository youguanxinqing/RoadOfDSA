package sorts

import (
	"testing"
)

func TestQuickSort(t *testing.T) {
	nums := []int{6, 3, 9, 10, 2, 1, 1, 2}
	QuickSort(nums)

	length := len(nums) - 1
	for i := 1; i <= length; i++ {
		if nums[i] < nums[i-1] {
			t.Error("quick sort error")
		}
	}
}
