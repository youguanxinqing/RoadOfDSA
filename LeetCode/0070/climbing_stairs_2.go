func climbStairs(n int) int {
    cache := make(map[int]int, 1000)
    return helper(n, cache)
}

func helper(n int, cache map[int]int) int {
    if n < 3 {
        return n
    }
    res := 0
    if val, ok := cache[n]; ok {
        res = val
    } else {
        res = helper(n-1, cache) + helper(n-2, cache)
        cache[n] = res
    }
    return res
}
