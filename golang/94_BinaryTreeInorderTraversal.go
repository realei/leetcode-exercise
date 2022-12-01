/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) (res []int) {
    dfs(root, &res)
    return res
}

func dfs(node *TreeNode, res *[]int) {
    if node == nil {
        return
    }
    
    dfs(node.Left, res)
    *res = append(*res, node.Val)
    dfs(node.Right, res)
}
