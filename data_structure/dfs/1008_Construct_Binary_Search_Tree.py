# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inorder = sorted(preorder) 
        def generateBinarySearchTree(pOrder, iOrder):
            if len(pOrder) == 0: return None
            root = TreeNode(pOrder[0])  # root node
            rootInx = iOrder.index(root.val)

            root.left = generateBinarySearchTree(pOrder[1:rootInx + 1], iOrder[0:rootInx + 1])
            root.right = generateBinarySearchTree(pOrder[rootInx+1:], iOrder[rootInx+1:])
            return root

        return generateBinarySearchTree(preorder,inorder)
