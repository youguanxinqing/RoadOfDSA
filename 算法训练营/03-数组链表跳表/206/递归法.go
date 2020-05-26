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
	if head == nil || head.Next == nil {
		return head
	}
	// reverseList 函数总是返回链表的头指针
	root := reverseList(head.Next)
	head.Next.Next = head
	head.Next = nil
	return root
}
// @lc code=end
