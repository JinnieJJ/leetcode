import "sort"
func largestDivisibleSubset(nums []int) []int {
    if len(nums) == 0 {
        return []int{}
    }
    sort.Ints(nums)
    
    parent := make([]int, len(nums))
    count := make([]int, len(nums))
    for i := 0; i < len(nums); i++ {
        parent[i] = -1
        count[i] = 1
    }
    max := 1
    max_index := 0
    for i := 0; i < len(nums); i++ {
        for j := i-1; j >= 0; j-- {
            if nums[i] % nums[j] == 0 && count[j] + 1 > count[i] {
                count[i] = count[j] + 1
                parent[i] = j
            }
        }
        if count[i] > max {
            max = count[i]
            max_index = i
        }
    }
    list := []int{}
    for i := max_index; i != -1; i = parent[i] {
        list = append(list, nums[i])
    }
    result := []int{}
	for i := len(list) - 1; i >= 0; i-- {
		result = append(result, list[i])
	}
	return result

}
