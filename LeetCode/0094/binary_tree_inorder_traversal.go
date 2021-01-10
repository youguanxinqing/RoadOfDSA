/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func inorderTraversal(root *TreeNode) []int {
    p := &[]int{}
    return helper(root, p)
}

func helper(root *TreeNode, p *[]int) []int {
    if root != nil {
        helper(root.Left, p)
        res := append(*p, root.Val)
        *p = res
        helper(root.Right, p)
    }
    return *p
}
