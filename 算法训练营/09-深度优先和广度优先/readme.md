# 模板

## DFS

二叉树：
```python
## 递归版本
def dfs(node):
    if node in visited:
        # already visited
        return
    visited.add(node)

    # process current node
    # ... # logic here
    dfs(node.left)
    dfs(node.right)

## 非递归版本
```

多叉树：
```python
def dfs(node, visited):
    if node in visited:
        # already visited
        return

    visited.add(node)

    # process current node
    # ...   
    for next_node in node.children():
        if next_node not in visited:
            dfs(next_node, visited)
```

## BFS

二叉树：
```python
## ...
```

多叉树：
```python
## ...
```

# 实战题目

- https://leetcode-cn.com/problems/binary-tree-level-order-traversal/#/description
- https://leetcode-cn.com/problems/minimum-genetic-mutation/#/description
- https://leetcode-cn.com/problems/generate-parentheses/#/description
- https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/#/description

# 课后作业

- https://leetcode-cn.com/problems/word-ladder/description/
- https://leetcode-cn.com/problems/word-ladder-ii/description/
- https://leetcode-cn.com/problems/number-of-islands/
- https://leetcode-cn.com/problems/minesweeper/description/
