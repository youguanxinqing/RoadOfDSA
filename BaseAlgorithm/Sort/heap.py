from typing import List

import heapq


def heap_sort(arr: List):
    q = []
    for item in arr:
        heapq.heappush(q, item)
    
    ret = []
    for _ in range(len(arr)):
        ret.append(heapq.heappop(q))

    return ret


def test_heap_sort(num: int):
    import random
    unsorted_array = [random.randrange(0, 100) for _ in range(num)]
    print(f"unsorted_array: {unsorted_array}")
    
    print(sorted(unsorted_array) == heap_sort(unsorted_array))


if __name__ == "__main__":
    test_heap_sort(10)
