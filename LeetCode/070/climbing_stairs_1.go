func climbStairs(n int) int {
    if (n <=2 ) {
        return n
    }
    n1, n2 := 1, 2
    res := 0
    for n >= 3 {
        res = n1 + n2
        n1, n2 = n2, res
        n--
    }
    return res
}
