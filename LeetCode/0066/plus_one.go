func plusOne(digits []int) []int {
    length := len(digits) - 1
    for i:=length; i >= 0; i-- {
        digits[i] += 1
        digits[i] %= 10
        if digits[i] != 0 {
            return digits
        }
    }
    newDigits := []int{1}
    return append(newDigits, digits...)
}
