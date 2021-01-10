/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
    HEAD := &ListNode{Next: head}
    pre, nxt := HEAD, HEAD.Next
    for nxt != nil && nxt.Next != nil {
        pre.Next = nxt.Next
        nxt.Next = pre.Next.Next
        pre.Next.Next = nxt

        pre = nxt
        nxt = nxt.Next
    }
    return HEAD.Next
}
