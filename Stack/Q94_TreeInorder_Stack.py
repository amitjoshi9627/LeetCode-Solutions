'''

LeetCode Q.91 Binary Tree Inorder Traversal
Iterative Solution	

'''


def inorderTraversal(self, root: TreeNode) -> List[int]:
    stack = []
    inorder = []
    while True:
        if root:
            stack.append(root)
            root = root.left
        elif stack:
            root = stack.pop(-1)
            inorder.append(root.val)
            root = root.right

        else:
            return inorder
