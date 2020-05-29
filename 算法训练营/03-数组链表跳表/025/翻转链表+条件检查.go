/*
 * @lc app=leetcode.cn id=25 lang=golang
 *
 * [25] K 个一组翻转链表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseKGroup(head *ListNode, k int) *ListNode {
	if k == 0 || k == 1 {
		return head
	}
	
	root := new(ListNode)
	root.Next = head
	pre, cur := root, root
	for {
		// 检查是否满足翻转条件
		for i:=0; i<k; i++ {
			if cur != nil && cur.Next != nil {
				cur = cur.Next
			} else {
				return root.Next
			}
		}
		// 翻转
		tail := reverse(pre, k)
		pre, cur = tail, tail
	}
}

func reverse(start *ListNode, k int) *ListNode {
	tail := start.Next	
	for ; k>1; k-- {
		tmp := tail.Next.Next
		tail.Next.Next = start.Next
		start.Next = tail.Next
		tail.Next = tmp
	}
	return tail
}
// @lc code=end
