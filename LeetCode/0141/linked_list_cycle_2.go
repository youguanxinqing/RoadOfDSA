/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    if head != nil {
        record := make(map[*ListNode]int, 100)
        for head != nil {
            if _, ok := record[head]; ok {
                return true
            }
            record[head] = 0
            head = head.Next
        }
    }
    return false
}
