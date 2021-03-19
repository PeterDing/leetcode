class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def st(r1, r2):
    if not r1 and not r2:
        return True

    if not r1 and r2:
        return False
    if r1 and not r2:
        return False
    if r1.val != r2.val:
        return False

    return st(r1.left, r2.left) and st(r1.right, r2.right)
