# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder(root: TreeNode, vals):
    s = 0
    vals.append(root.val)
    if root.left:
        s += preorder(root.left, vals)
    if root.right:
        s += preorder(root.right, vals)
    if not root.left and not root.right:
        path_val = 0
        for i, val in enumerate(vals[::-1]):
            path_val += val * (10**i)
        s += path_val
    vals.pop()
    return s


def sumNumbers(root: TreeNode) -> int:
    if not root:
        return 0

    return preorder(root, [])
