/*
 * @lc app=leetcode.cn id=142 lang=golang
 *
 * [142] 环形链表 II
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
	nth := 0
	records := make(map[*ListNode]int)
	for head != nil {
		_, ok := records[head]
		if ok { // 环
			return head
		}
		records[head] = nth
		nth++
		head = head.Next
	}
	return nil
}
// @lc code=end
