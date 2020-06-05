/*
 * @lc app=leetcode.cn id=54 lang=rust
 *
 * [54] 螺旋矩阵
 */

// @lc code=start
impl Solution {
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
        let mut rets: Vec<i32> = Vec::new();
        if matrix.len() == 0 {
            return rets;
        }
        let (mut yMin, mut yMax) = (0usize, matrix.len());
        let (mut xMin, mut xMax) = (0usize, matrix[0].len());
        loop {
            for x in xMin..xMax {
                rets.push(matrix[yMin][x]);
            }
            yMin += 1;
            if yMin == yMax {
                break;
            }

            for y in yMin..yMax {
                rets.push(matrix[y][xMax-1]);
            }
            xMax -= 1;
            if xMin == xMax {
                break;
            }

            for x in (xMin..xMax).rev() {
                rets.push(matrix[yMax-1][x]);
            }
            yMax -= 1;
            if yMin == yMax {
                break;
            }

            for y in (yMin..yMax).rev() {
                rets.push(matrix[y][xMin]);
            }
            xMin += 1;
            if xMin == xMax {
                break;
            }
        }
        return rets;
    }
}
// @lc code=end
