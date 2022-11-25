func twoSum(nums []int, target int) []int {
    var hashMap map[int]int
    hashMap = make(map[int]int)

    for k, v := range nums {
        if val, ok := hashMap[target - v]; ok {
            return []int{val, k}
        }
        hashMap[v] = k
    }
    return nil
}
