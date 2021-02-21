# 二分查找的前提

1. 目标函数单调性（单调递增或递减）
2. 存在上下界（bounded）
3. 能够通过索引访问（index accessible）

# 模板

```python
left, right = 0, len(array)-1
while left <= right:
    mid = (left + right) // 2
    if array[mid] == target:
        # find the targe
        break or return result
    elif array[mid] < mid:
        low = mid + 1
    else:
        high = mid - 1
```