package main

import "fmt"

type UnionFind struct {
	data []int
}

func New(min, max int) *UnionFind {
	data := make([]int, max-min)
	for i := min; i < max; i++ {
		data[i] = i
	}
	return &UnionFind{
		data: data,
	}
}

// Find: 寻找元素的 root
func (uf *UnionFind) Find(i int) int {
	if i != uf.data[i] {
		uf.data[i] = uf.Find(uf.data[i])
	}
	return uf.data[i]
}

// union: 合并两个集合
func (uf *UnionFind) Union(i int, j int) {
	pi, pj := uf.Find(i), uf.Find(j)
	if pi != pj {
		uf.data[pi] = uf.data[pj]
	}
}

func (uf *UnionFind) IsConnected(i int, j int) bool {
	return uf.Find(i) == uf.Find(j)
}

func main() {
	// 元素之间的关系
	connections := [][]int{
		{0, 1}, {1, 2}, {0, 9},
		{5, 6}, {6, 4}, {3, 8},
	}

	uFind := New(0, 10)
	for _, connection := range connections {
		i, j := connection[0], connection[1]
		uFind.Union(i, j)
	}

	fmt.Println(uFind.data)
	/*
	 *  (0, 1, 2, 9)
	 *  (5, 6, 4)
	 *  (3, 8)
	**/

	// test
	for _, cons := range [][]int{{4, 9}, {0, 9}, {3, 9}} {
		i, j := cons[0], cons[1]
		isConnected := uFind.IsConnected(i, j)
		fmt.Printf("%d - %d (%v)\n", i, j, isConnected)
	}
}
