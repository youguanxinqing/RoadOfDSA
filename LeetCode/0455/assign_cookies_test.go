package assign_cookies

import "testing"

func TestFindContentChildren(t *testing.T) {
	var (
		g1 = []int{1, 2, 3}
		s1 = []int{1, 1}

		g2 = []int{1, 2}
		s2 = []int{1, 2, 3}
	)
	res := findContentChildren(g1, s1)
	if res != 1 {
		t.Errorf("error: %v\n", res)
	}

	res = findContentChildren(g2, s2)
	if res != 2 {
		t.Errorf("error: %v\n", res)
	}
}
