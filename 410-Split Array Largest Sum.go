func splitArray(nums []int, m int) int {
    n := len(nums)
    dp := make([][]int, n+1)
    for i := 0; i <= n; i++ {
        dp[i] = make([]int, m+1)
        for j := 0; j <= m; j++ {
            dp[i][j] = math.MaxInt32
        }
    }
    sub := make([]int, n+1)
    for i := 0; i < n; i++ {
        sub[i+1] = sub[i] + nums[i]
    }
    dp[0][0] = 0
    for i := 1; i <= n; i++ {
        for j := 1; j <= m; j++ {
            for k := 0; k < i; k++ {
                dp[i][j] = min(dp[i][j], max(dp[k][j-1], sub[i]-sub[k]))
            }
        }
    }
    return dp[n][m]
}

func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a int, b int) int {
    if a < b {
        return a
    }
    return b
}
