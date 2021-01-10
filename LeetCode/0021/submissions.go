/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {

    var head ListNode
    p := &head

    for {
        if l1 == nil || l2 == nil {
            break
        } else if l1.Val < l2.Val {
            p.Val = l1.Val
            l1 = l1.Next
        } else {
            p.Val = l2.Val
            l2 = l2.Next
        }

        p.Next = &ListNode{}
        p = p.Next
    }
    
    if l1 != nil {
        *p = *l1
    } else if l2 != nil {
        *p = *l2
    } else {
        return nil
    }
    return &head
}
