package main

import (
    "fmt"
)

func countBits(num int) []int {
    record := make(map[int]int, 1000)
    record[0], record[1] = 0, 1
    return countBitsHelper(num, record)
}

func countBitsHelper(num int, record map[int]int) []int {
    for i:=0; i<=num; i++ {
        count = 0
        if val, ok := record[i]; ok {
            count = val
        } else {
            count & (i)
        }
    }
}

func main() {
    res := countBits(1)
    fmt.Println(res)
}
