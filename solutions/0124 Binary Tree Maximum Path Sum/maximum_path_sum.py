import math


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def generate_max_sum_path(root, m):
    if not root:
        return

    if root.left:
        m = max(m, generate_max_sum_path(root.left, m))
    if root.right:
        m = max(m, generate_max_sum_path(root.right, m))

    # the max path sum from root to a leaf
    # which is equal:
    root.m = max(
        root.val,
        root.val + root.left.m if root.left else -math.inf,
        root.val + root.right.m if root.right else -math.inf,
    )

    # So, the max sum path is:
    return max(
        m,
        root.m,
        root.val + (root.left.m if root.left else -math.inf) +
        (root.right.m if root.right else -math.inf),
    )


def mps(root):
    m = generate_max_sum_path(root, -math.inf)
    return m


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

s = mps(root)

print(s)
