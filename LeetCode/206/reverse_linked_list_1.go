/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    var newHead *ListNode

	for head != nil {
        node := ListNode{head.Val, nil}
        head = head.Next
        if newHead == nil {
            newHead = &node
        } else {
            node.Next = newHead
            newHead = &node
        }
    }

	return newHead
}
