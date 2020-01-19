func hammingWeight(num uint32) int {
    counter := 0
    for {
        if num & 1 == 1 {
            counter += 1
        }
        num = num >> 1
        if num == 0 {
            break
        }
    }
    return counter
}
