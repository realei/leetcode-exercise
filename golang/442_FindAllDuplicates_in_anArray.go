func findDuplicates(nums []int) []int {
    var res []int
    seen := make(map[int]int) 

    for _, v := range nums {
        _, ok := seen[v]
        if !ok {
            seen[v] = 1
        } else {
            seen[v]++
        }
    }

    for k, v := range seen {
        if v > 1 {
            res = append(res, k)
        }
    }

    return res
}
