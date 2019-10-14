package main

import (
	"errors"
	"fmt"
)

// BinarySearch 二分查找
func BinarySearch(elem int, arr []int) (int, error) {
	l := 0
	r := len(arr)

	for l < r {
		// var mid int = (r - 1 + l) / 2
		mid := l + ((r - 1 - l) >> 1) // 位运算实现极致优化
		if elem < arr[mid] {
			r = mid
		} else if elem > arr[mid] {
			l = mid + 1
		} else {
			return mid, nil
		}
	}

	return -1, errors.New("elem not exsited")
}

func main() {
	// test...
	arr := []int{1, 10, 12, 13, 100, 654}

	if i, err := BinarySearch(2, arr); err == nil {
		fmt.Println(i)
	} else {
		fmt.Println(err)
	}

	if i, err := BinarySearch(13, arr); err == nil {
		fmt.Println(i)
	} else {
		fmt.Println(err)
	}

	if i, err := BinarySearch(654, arr); err == nil {
		fmt.Println(i)
	} else {
		fmt.Println(err)
	}
}
