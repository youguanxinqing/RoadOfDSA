/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
    if head != nil {
        record := make(map[*ListNode]int, 100)
        for head != nil {
            if _, ok := record[head]; ok {
                return head
            }
            record[head] = 0
            head = head.Next
        }
    }
    return nil
}
