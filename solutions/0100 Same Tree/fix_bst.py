import math


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder_tree(root, rs):
    if not root:
        return
    inorder_tree(root.left, rs)
    rs.append(root)
    inorder_tree(root.right, rs)


def fix_bst(root):
    rs = [TreeNode(-math.inf)]
    inorder_tree(root, rs)
    rs.append(TreeNode(math.inf))

    err_nodes = []
    for i in range(len(rs) - 2):
        if rs[i].val < rs[i + 1].val and rs[i + 1].val > rs[i + 2].val:
            err_nodes.append(rs[i + 1])
        if rs[i].val > rs[i + 1].val and rs[i + 1].val < rs[i + 2].val:
            err_nodes.append(rs[i + 1])

    a = err_nodes[0]
    b = err_nodes[-1]
    a.val, b.val = b.val, a.val
