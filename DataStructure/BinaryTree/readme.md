# 树与图的差别

是否存在环。

# 节点表示

- **python**
```python
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
```

- **c++**
```cpp
class TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int val): val(val), left(NULL), right(NULL) {}
}
```

# 树的遍历 

1. 前: root - left - right
2. 中: left - root - right 
3. 后: left - right - root

记忆方式：“前中后”针对与 root，left 总在 right 的右边。

# 二叉搜索树

1. 左子树所有结点小于根结点的值。
2. 右子树所有结点大于根结点的值。
3. 左子树和右子树重复上述规定。

时间复杂度：查询、删除、插入都是 logn。


