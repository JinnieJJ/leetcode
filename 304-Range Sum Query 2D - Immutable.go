type NumMatrix struct {
    dp [][]int
}


func Constructor(matrix [][]int) NumMatrix {
    if len(matrix) == 0 || len(matrix[0]) == 0 {
        return NumMatrix{}
    }
    d := make([][]int, len(matrix)+1)
    for i := 0; i <= len(matrix); i++ {
        d[i] = make([]int, len(matrix[0])+1)
    }
    for i := 0; i < len(matrix); i++ {
        for j := 0; j < len(matrix[0]); j++ {
            d[i+1][j+1] = d[i+1][j] + d[i][j+1] - d[i][j] + matrix[i][j]
        }
    }
    return NumMatrix {
        dp: d,
    }
}


func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    return this.dp[row2+1][col2+1] - this.dp[row1][col2+1] - this.dp[row2+1][col1] + this.dp[row1][col1]
}


/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
 */
