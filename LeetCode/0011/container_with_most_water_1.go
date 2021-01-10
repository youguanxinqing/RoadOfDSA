func maxArea(height []int) int {
    maxAreaVal, areaVal := 0, 0
    i, j := 0, len(height) - 1
    for i < j {
        if height[i] < height[j] {
            areaVal = height[i] * (j - i)
            i++
        } else {
            areaVal = height[j] * (j - i)
            j--
        }
        if areaVal > maxAreaVal {
            maxAreaVal = areaVal
        }
    }
    return maxAreaVal
}
