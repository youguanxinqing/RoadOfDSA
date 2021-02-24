from typing import List


def merge_sort(arr: List):
    if len(arr) <= 1:
        return arr
        
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    l, r = 0, 0
    
    ret = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            ret.append(left[l])
            l += 1
        else:
            ret.append(right[r])
            r += 1
    
    ret += left[l:]
    ret += right[r:]
    
    return ret


def test_merge_sort(num: int):
    import copy
    import random
    unsorted_array = [random.randrange(0, 100) for _ in range(10)]
    print(f"unsorted_array: {unsorted_array}")
    
    print(sorted(unsorted_array) == merge_sort(unsorted_array))


if __name__ == "__main__":
    test_merge_sort(10)
