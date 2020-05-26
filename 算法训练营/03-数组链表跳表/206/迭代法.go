/*
 * @lc app=leetcode.cn id=206 lang=golang
 *
 * [206] 反转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
	root := new(ListNode)
	for head != nil {
		tmp := root.Next 
		root.Next = head
		head = head.Next
		root.Next.Next = tmp // 最后赋值末尾, 顺序不能乱
	}
	return root.Next
}
// @lc code=end