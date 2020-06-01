/*
 * @lc app=leetcode.cn id=21 lang=golang
 *
 * [21] 合并两个有序链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	root := new(ListNode)
	cur := root
	for l1 != nil && l2 != nil {
		for l1 != nil && l1.Val <= l2.Val {
			cur.Next = l1
			l1 = l1.Next
			cur = cur.Next
		}
		if l1 == nil {
			break
		}
		
		for l2 != nil && l2.Val < l1.Val {
			cur.Next = l2
			l2 = l2.Next
			cur = cur.Next
		}
	}

	if l1 == nil {
		cur.Next = l2
	} else {
		cur.Next = l1
	}
	return root.Next
}
// @lc code=end