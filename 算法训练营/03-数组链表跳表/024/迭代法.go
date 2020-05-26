/*
 * @lc app=leetcode.cn id=24 lang=golang
 *
 * [24] 两两交换链表中的节点
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
	root := new(ListNode)
	root.Next = head

	cur := root
	for cur.Next != nil && cur.Next.Next != nil {
		node := cur.Next.Next
		cur.Next.Next = node.Next
		node.Next = cur.Next
		cur.Next = node
		cur = cur.Next.Next
	}
	return root.Next
}

// @lc code=end
