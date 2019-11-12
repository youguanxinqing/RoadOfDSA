/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func swapPairs(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    node := swapPairs(head.Next.Next)
    temp := head.Next
    head.Next = node
    temp.Next = head
    return temp
}

