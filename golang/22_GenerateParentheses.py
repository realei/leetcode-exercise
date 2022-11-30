func generateParenthesis(n int) []string {

    if n == 0 {
        return []string{}
    }

    left, right := n-1, n
    cur := []byte{'('}
    var res []string

    dfs(left, right, cur, &res)
    return res
}

func dfs(left, right int, cur []byte, res *[]string) {
    if left == 0 && right == 0 {
        *res = append(*res, string(cur))
        return
    }
    
    if left > 0 {
        dfs(left-1, right, append(cur, '('), res)
    }

    if right > left {
        dfs(left, right-1, append(cur, ')'), res)
    }
}
