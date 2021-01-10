/**
 *  普通方法
**/

func hammingWeight(num uint32) int {
    counter := 0
    for {
        if num & 1 == 1 {
            counter += 1
        }
        if num = num >> 1; num == 0 {
            break
        }
    }
    return counter
}
