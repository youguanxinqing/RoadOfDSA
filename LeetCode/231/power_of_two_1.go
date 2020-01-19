func isPowerOfTwo(n int) bool {
    x := 1
    for {
        if x == n {
            return true
        } else if x > n {
            return false
        }
        x = x * 2
    }
}

