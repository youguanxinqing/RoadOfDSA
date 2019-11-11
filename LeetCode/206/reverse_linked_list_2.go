/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// 与方法 1 原理相同，但是代码更简洁 
func reverseList(head *ListNode) *ListNode {
    var (
        prev *ListNode
        cur *ListNode = head
        temp *ListNode
    )

	for cur != nil {
        temp = cur.Next
        cur.Next = prev
        prev = cur
        cur = temp
    }

    return prev
}
