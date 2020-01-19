package main

import (
    "fmt"
)

func reverseBits(num uint32) uint32 {
    for i:=uint32(0); i<16; i++ {
        // low 低位; high 高位
        low := num & (1<<i)
        high := num & (1<<(31-i))
        // 当高位，地位都为0或者1时，无需做交换处理
        // 反之则需要做交换处理
        if high | low != 0 && (low == 0 || high == 0) {
            if low == 0 { // 当低位为0，高位为1时
                num = num & (^(1<<(31-i)))
                num = num | (1<<i)
            } else { // 当低位有1，高位全为0时
                num = num | (1<<(31-i))
                num = num & (^(1<<i))
            }
        }   // 置0用&, 置1用｜
    }
    return num
}

func main() {
    x := uint32(12)
    res := reverseBits(x)
    fmt.Println(res)
}
