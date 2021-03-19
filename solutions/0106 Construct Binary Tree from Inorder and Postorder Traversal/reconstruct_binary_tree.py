class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# inorder:    |abc|d|efg|
#           left   up   right
# postorder:  |---|fge|d|

def reconstruct(inorder, postorder, istart, iend, pstart, pend):
    global postitions

    if iend - istart == 0:
        return None

    if iend - istart == 1:
        return TreeNode(inorder[istart])

    up = TreeNode(postorder[pend - 1])

    index = postitions[up.val]
    left = reconstruct(inorder, postorder, istart, index, pstart, pstart + index - istart)
    right = reconstruct(inorder, postorder, index + 1, iend, pstart + index - istart, pend - 1)

    up.left = left
    up.right = right

    return up


inorder = [2, 1]
postorder = [2, 1]
postitions = {c: i for i, c in enumerate(inorder)}
reconstruct(inorder, postorder, 0, len(inorder), 0, len(inorder))
