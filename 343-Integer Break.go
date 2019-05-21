func integerBreak(n int) int {
    var dp []int = make([]int, n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    for i := 3; i <= n; i++ {
        for j := 1; j < i; j ++ {
            dp[i] = max(dp[i], max(dp[j], j) * max(dp[i-j], i-j))
        }
    }
    return dp[n]
}

func max(a, b int) int {
    if (a > b) {
        return a
    }
    return b
}
