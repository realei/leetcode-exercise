func containsNearbyDuplicate(nums []int, k int) bool {
    seen := make(map[int]int)
    for i, v := range nums {
        if j, ok := seen[v]; ok && i-j <= k {
            return true
        }
        seen[v] = i
    }
    return false
}
