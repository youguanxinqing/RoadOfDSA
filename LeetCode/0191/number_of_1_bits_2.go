/**
 * 清除数值x二进制中最低位上的1: x & (x-1)
 * 相比方法1，循环次数更少
**/

func hammingWeight(num uint32) int {
    counter := 0
    for {
        if num == 0 {
            break
        }
        counter += 1
        num = num & (num-1)
    }
    return counter
}
