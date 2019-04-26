# 0226 - Invert Binary Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Tree | [Leetcode](https://leetcode.com/problems/invert-binary-tree) | [solution](https://leetcode.com/problems/invert-binary-tree/solution/)


-----------

<p>Invert a binary tree.</p>

<p><strong>Example:</strong></p>

<p>Input:</p>

<pre>
     4
   /   \
  2     7
 / \   / \
1   3 6   9</pre>

<p>Output:</p>

<pre>
     4
   /   \
  7     2
 / \   / \
9   6 3   1</pre>

<p><strong>Trivia:</strong><br />
This problem was inspired by <a href="https://twitter.com/mxcl/status/608682016205344768" target="_blank">this original tweet</a> by <a href="https://twitter.com/mxcl" target="_blank">Max Howell</a>:</p>

<blockquote>Google: 90% of our engineers use the software you wrote (Homebrew), but you can&rsquo;t invert a binary tree on a whiteboard so f*** off.</blockquote>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach #1 (Recursive) [Accepted]


This is a classic tree problem that is best-suited for a recursive approach.


**Algorithm**

The inverse of an empty tree is the empty tree. The inverse of a tree with root $$r$$, and subtrees $$\mbox{right}$$ and $$\mbox{left}$$, is a tree with root $$r$$, whose right subtree is the inverse of $$\mbox{left}$$, and whose left subtree is the inverse of $$\mbox{right}$$.

**Java**

```java
public TreeNode invertTree(TreeNode root) {
    if (root == null) {
        return null;
    }
    TreeNode right = invertTree(root.right);
    TreeNode left = invertTree(root.left);
    root.left = right;
    root.right = left;
    return root;
}
```

**Complexity Analysis**

Since each node in the tree is visited only once, the time complexity is $$O(n)$$, where $$n$$ is the number of nodes in the tree. We cannot do better than that, since at the very least we have to visit each node to invert it.

Because of recursion, $$O(h)$$ function calls will be placed on the stack in the worst case, where $$h$$ is the height of the tree. Because $$h\in O(n)$$, the space complexity is $$O(n)$$.

---
#### Approach #2 (Iterative) [Accepted]

Alternatively, we can solve the problem iteratively, in a manner similar to breadth-first search.

**Algorithm**

The idea is that we need to swap the left and right child of all nodes in the tree. So we create a queue to store nodes whose left and right child have not been swapped yet. Initially, only the root is in the queue. As long as the queue is not empty, remove the next node from the queue, swap its children, and add the children to the queue. Null nodes are not added to the queue. Eventually, the queue will be empty and all the children swapped, and we return the original root.

**Java**
```java
public TreeNode invertTree(TreeNode root) {
    if (root == null) return null;
    Queue<TreeNode> queue = new LinkedList<TreeNode>();
    queue.add(root);
    while (!queue.isEmpty()) {
        TreeNode current = queue.poll();
        TreeNode temp = current.left;
        current.left = current.right;
        current.right = temp;
        if (current.left != null) queue.add(current.left);
        if (current.right != null) queue.add(current.right);
    }
    return root;
}
```

**Complexity Analysis**

Since each node in the tree is visited / added to the queue only once, the time complexity is $$O(n)$$, where $$n$$ is the number of nodes in the tree.

Space complexity is $$O(n)$$, since in the worst case, the queue will contain all nodes in one level of the binary tree. For a full binary tree, the leaf level has $$\lceil \frac{n}{2}\rceil=O(n)$$ leaves.

Analysis written by: @noran
