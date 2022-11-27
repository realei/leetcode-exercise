func twoSum(nums []int, target int) []int {
    // constant space
    hashMap := make(map[int]int, len(nums))

    for k, v := range nums {
        if val, ok := hashMap[target - v]; ok {
            return []int{val, k}
        }
        hashMap[v] = k
    }
    return nil
}
