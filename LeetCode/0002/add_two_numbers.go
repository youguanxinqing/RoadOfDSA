/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var l ListNode = ListNode{}
	p := &l
	var prev *ListNode

	step := 0
	for l1 != nil || l2 != nil || step != 0 {
		n := 0
		if l1 != nil && l2 != nil {
			n = l1.Val + l2.Val
			l1 = l1.Next
			l2 = l2.Next
		} else if l1 != nil && l2 == nil {
			n = l1.Val
			l1 = l1.Next
		} else if l1 == nil && l2 != nil {
			n = l2.Val
			l2 = l2.Next
		}

		n2 := (step + n) % 10
		prev = p
		p.Val = n2
		p.Next = &ListNode{}
		p = p.Next
		step = (step + n - n2) / 10
	}

	if prev != nil {
		prev.Next = nil
	}

	return &l
}
