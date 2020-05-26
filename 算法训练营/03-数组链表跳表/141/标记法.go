/*
 * @lc app=leetcode.cn id=141 lang=golang
 *
 * [141] 环形链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
	records := make(map[*ListNode]bool)
	for head != nil {
		if records[head] {
			return true
		}
		records[head] = true
		head = head.Next
	}
	return false
}
// @lc code=end