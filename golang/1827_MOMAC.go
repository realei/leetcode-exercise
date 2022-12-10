func max(a, b int) int {
    if b > a {
        return b
    }
    return a
}


func minOperations(nums []int) (res int) {
    pre := nums[0] - 1
    for _, x := range nums {
        pre = max(pre+1, x)
        res += pre - x
    }
    return
}
