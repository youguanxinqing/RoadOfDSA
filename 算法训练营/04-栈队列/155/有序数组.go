/*
 * @lc app=leetcode.cn id=155 lang=golang
 *
 * [155] 最小栈
 */

// @lc code=start
type MinStack struct {
	Vals  []int  // 维护插入顺序
	OrderVals []int  // 维护值大小顺序
	Length int
}


/** initialize your data structure here. */
func Constructor() MinStack {
	p := new(MinStack)
	return *p
}


func (this *MinStack) Push(x int)  {
	// 值顺序
	l, r := 0, this.Length-1
	mid := -1
	for l <= r {
		mid = (r - l) / 2 + l
		switch {
		case x > this.OrderVals[mid]:
			l = mid+1
		case x == this.OrderVals[mid]:
			goto afterLoop  // 找到相同值
		case x < this.OrderVals[mid]:
			r = mid-1
		}
	}
afterLoop:
	var loc int
	if mid < 0 {
		this.OrderVals = append(this.OrderVals, x)
	} else {
		if this.OrderVals[mid] > x {
			loc = mid
		} else {
			loc = mid+1
		}
		this.OrderVals = append(
			this.OrderVals[:loc], 
			append([]int{x}, this.OrderVals[loc:]...)...)
	}
	
	// 插入顺序
	this.Vals = append(this.Vals, x)
	this.Length++
}

// 根据要求，这里未做过多的参数校验
func (this *MinStack) Pop()  {
	x := this.Top()
	l, r := 0, this.Length-1
	var mid int
	for l <= r {
		mid = (r - l) / 2 + l
		switch {
		case x > this.OrderVals[mid]:
			l = mid+1
		case x == this.OrderVals[mid]:
			goto afterLoop  // 找到相同值
		case x < this.OrderVals[mid]:
			r = mid-1
		}
	}
afterLoop:
	this.OrderVals = append(
		this.OrderVals[:mid], this.OrderVals[mid+1:]...)

	this.Length--
	this.Vals = this.Vals[:this.Length]
}


func (this *MinStack) Top() int {
	return this.Vals[this.Length-1]
}


func (this *MinStack) GetMin() int {
	return this.OrderVals[0]
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
// @lc code=end