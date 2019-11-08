func maxArea(height []int) int {
    maxAreaVal, areaVal := 0, 0
    for i, vali := range height {
        for j, valj := range height[i+1:] {
            if vali < valj {
                areaVal = vali * (j + 1)
            } else {
                areaVal = valj * (j + 1)
            }
            if areaVal > maxAreaVal {
                maxAreaVal = areaVal
            }
        }
    }
    return maxAreaVal
}
