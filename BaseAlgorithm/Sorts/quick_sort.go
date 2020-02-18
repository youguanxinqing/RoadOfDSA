package sorts

func QuickSort(arr []int) {
	if len(arr) <= 1 {
		return
	}
	sort(arr, 0, len(arr)-1)
}

func sort(arr []int, low, high int) {
	if low >= high {
		return
	}

	p := arr[low] // 获取一个基准点
	l, r := low, high
	for l < r {
		for arr[r] >= p && l < r {
			r--
		}
		arr[l] = arr[r]
		for arr[l] <= p && l < r {
			l++
		}
		arr[r] = arr[l]
	}
	arr[l] = p

	sort(arr, 0, l-1)
	sort(arr, l+1, high)
}
