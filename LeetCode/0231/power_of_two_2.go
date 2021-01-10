/**
 * 作为2的幂的整数，应该有且只有一个1
**/

func isPowerOfTwo(n int) bool {
    if n <= 0 {
        return false
    }
    if n = n & (n-1); n == 0 {
        return true
    } else {
        return false
    }
}
