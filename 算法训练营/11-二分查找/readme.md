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

# 习题

## 实战题目

- https://leetcode-cn.com/problems/sqrtx/
- https://leetcode-cn.com/problems/valid-perfect-square/

## 课后作业

- https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
- https://leetcode-cn.com/problems/search-a-2d-matrix/
- https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/
