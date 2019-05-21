func longestPalindromeSubseq(s string) int {
    n := len(s)
    dp := make([][]int, n)
    for i := 0; i < n; i++ {
        dp[i] = make([]int, n)
    }
    for i := 0; i < n; i++ {
        dp[i][i] = 1
    }
    for gap := 1; gap < n; gap++ {
        j := 0
        for i := 0; j < n; i++ {
            j = i + gap
            if s[i] == s[j] {
                dp[i][j] = dp[i+1][j-1] + 2
            } else {
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            }
            j++
        }
    }
    return dp[0][n-1]
}

func max(a int, b int) int {
    if a > b{
        return a
    }
    return b
}
