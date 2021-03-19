# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def inorder(root: TreeNode, stock: list) -> None:
    if root.left:
        inorder(root.left, stock)
    stock.append(root)
    if root.right:
        inorder(root.right, stock)


def recoverTree(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if not root:
        return

    wrapeds = []
    nodes = []
    inorder(root, nodes)
    for i in range(len(nodes) - 1):
        if nodes[i].val > nodes[i + 1].val:
            wrapeds.append(i)

    if len(wrapeds) == 0:
        return
    elif len(wrapeds) == 1:  # wrap i and i+1
        i = wrapeds[0]
        ii = i + 1
        nodes[i].val, nodes[ii].val = nodes[ii].val, nodes[i].val
    elif len(wrapeds) == 2:  # wrap i and j, |i-j|>1
        i = wrapeds[0]
        ii = wrapeds[1] + 1  # Assume i, j are wraped, let k = wraped[ii], then nodes[k].val > nodes[k+1].val. Because nodes[i].val > nodes[j].val, so j = k+1
        nodes[i].val, nodes[ii].val = nodes[ii].val, nodes[i].val
    else:
        raise TypeError
