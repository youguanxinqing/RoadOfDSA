from typing import List

# way1
def quick_sort(arr: List, low: int, high: int):
    if low >= high:
        return

    left, right = low, high
    key = arr[left]
    while left != right:
        while left < right and key <= arr[right]:
            right -= 1
        arr[left] = arr[right]
        while left < right and key >= arr[left]:
            left += 1
        arr[right] = arr[left]
    arr[left] = key

    quick_sort(arr, low, left-1)
    quick_sort(arr, left+1, high)


def test_quick_sort(num: int):
    import copy
    import random
    unsorted_array = [random.randrange(0, 100) for _ in range(10)]
    print(f"unsorted_array: {unsorted_array}")
    
    quick_sort(unsorted_array, 0, len(unsorted_array)-1)
    print(sorted(copy.deepcopy(unsorted_array)) == unsorted_array)


if __name__ == "__main__":
    test_quick_sort(10)
