# 0199 - Binary Tree Right Side View

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree, Depth-first Search, Breadth-first Search | [Leetcode](https://leetcode.com/problems/binary-tree-right-side-view) | [solution](https://leetcode.com/problems/binary-tree-right-side-view/solution/)


-----------

<p>Given a binary tree, imagine yourself standing on the <em>right</em> side of it, return the values of the nodes you can see ordered from top to bottom.</p>

<p><strong>Example:</strong></p>

<pre>
<strong>Input:</strong>&nbsp;[1,2,3,null,5,null,4]
<strong>Output:</strong>&nbsp;[1, 3, 4]
<strong>Explanation:
</strong>
   1            &lt;---
 /   \
2     3         &lt;---
 \     \
  5     4       &lt;---
</pre>

-----------


## Similar Problems

- [Medium] [Populating Next Right Pointers in Each Node](populating-next-right-pointers-in-each-node)

- [Medium] [Boundary of Binary Tree](boundary-of-binary-tree)




## Solution:

[TOC]

#### Initial Thoughts

Because the tree topography is unknown ahead of time, it is not possible to
design an algorithm that visits asymptotically fewer than $$n$$ nodes.
Therefore, we should try to aim for a linear time solution. With that in
mind, let's consider a few equally-efficient solutions.

#### Approach #1 Depth-First Search [Accepted]

**Intuition**

We can efficiently obtain the right-hand view of the binary tree if we visit
each node in the proper order.

**Algorithm**

One of the aforementioned orderings is defined by a depth-first search in
which we always visit the right subtree first. This guarantees that the first
time we visit a particular depth of the tree, the node that we are visiting
is the rightmost node at that depth. Therefore, we can store the value of the
first node that we visit at each depth, ultimately generating a final array
of values once we know exactly how many layers are in the tree.

![Depth-First Search](../Figures/199/199_depth_first.png)
{:align="center"}

The figure above illustrates one instance of the problem. The red nodes
compose the solution from top to bottom, and the edges are labelled in order
of visitation.

<iframe src="https://leetcode.com/playground/U8377M7P/shared" frameBorder="0" width="100%" height="500" name="U8377M7P"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$.

    Because a binary tree with only child pointers is _directed acyclic graph_
    with only one source node, a traversal of the tree from the root will visit
    each node exactly once (plus a sublinear amount of leaves, represented as
    `None`). Each visitation requires only $$O(1)$$ work, so the while loop
    runs in linear time. Finally, building the array of rightmost values is
    $$O($$height of the tree$$) = O(n)$$ because it is not possible for a
    right-hand view of the tree to contain more nodes than the tree itself.

* Space complexity : $$O(n)$$.

    At worst, our stack will contain a number of nodes close to the height of
    the tree. Because we are exploring the tree in a depth-first order, there
    are never two nodes from different subtrees of the same parent node on the
    stack at once. Said another way, the entire right subtree of a node will be
    visited before any nodes of the left subtree are pushed onto the stack. If
    this logic is applied recursively down the tree, it follows that the stack
    will be largest when we have reached the end of the tree's longest path
    (the height of the tree). However, because we know nothing about the tree's
    topography, the height of the tree may be equivalent to $$n$$, causing the
    space complexity to degrade to $$O(n)$$.

---

#### Approach #2 Breadth-First Search [Accepted]

**Intuition**

Much like depth-first search can guarantee that we visit a depth's rightmost
node first, breadth-first search can guarantee that we visit it _last_.

**Algorithm**

By performing a breadth-first search that enqueues the left child before the
right child, we visit each node in each layer from left to right. Therefore,
by retaining only the most recently visited node per depth, we will have
the rightmost node for each depth once we finish the tree traversal. The
algorithm is unchanged, other than swapping out the stack for a
`deque`[^1] and removing the containment check before assigning into
`rightmost_value_at_depth`.

![Breadth-first Search Example](../Figures/199/199_breadth_first.png)
{:align="center"}

The figure above illustrates the same instance as before, but solved via
breadth-first search. The red nodes compose the solution from top to bottom,
and the edges are labelled in order of visitation.

<iframe src="https://leetcode.com/playground/9Aia2BUi/shared" frameBorder="0" width="100%" height="500" name="9Aia2BUi"></iframe>

**Complexity Analysis**

* Time complexity : $$O(n)$$.

    The differences itemized in the **Algorithm** section do not admit
    differences in the time complexity analysis between the bread-first and
    depth-first search approaches.

* Space complexity : $$O(n)$$.

    Because breadth-first search visits the tree layer-by-layer, the queue
    will be at its largest immediately before visiting the largest layer. The
    size of this layer is $$0.5n = O(n)$$ in the worst case (a complete binary
    tree).

---

**Footnotes**

[^1]: The
[`deque`](https://docs.python.org/3/library/collections.html#collections.deque)
datatype from the
[`collections`](https://docs.python.org/3/library/collections.html) module
supports constant time append/pop from both the head and the tail. If we were
to use a Python `list`, it would cost us $$O(n)$$ time to remove its head via
`list.pop(0)`.

---

Analysis written by: [@emptyset](https://leetcode.com/emptyset)
