/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func postorderTraversal(root *TreeNode) []int {
    p := &[]int{}
    return helper(root, p)
}

func helper(root *TreeNode, p *[]int) []int {
    if root != nil {
        helper(root.Left, p)
        helper(root.Right, p)
        *p = append(*p, root.Val)
    }
    return *p
}
