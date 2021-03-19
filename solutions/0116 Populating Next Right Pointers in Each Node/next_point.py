class Node:

    def __init__(
        self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def npp(nodes):
    if not nodes:
        return

    if len(nodes) > 1:
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

    sub_nodes = []
    for node in nodes:
        if node.left:
            sub_nodes.append(node.left)
        if node.right:
            sub_nodes.append(node.right)

    npp(sub_nodes)
