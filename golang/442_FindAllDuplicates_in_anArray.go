func findDuplicates(nums []int) (res []int) {
    seen := make(map[int]int, len(nums)) 

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
