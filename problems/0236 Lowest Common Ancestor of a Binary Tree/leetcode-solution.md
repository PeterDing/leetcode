# 0236 - Lowest Common Ancestor of a Binary Tree

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree | [Leetcode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree) | [solution](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/)


-----------

<p>Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.</p>

<p>According to the <a href="https://en.wikipedia.org/wiki/Lowest_common_ancestor" target="_blank">definition of LCA on Wikipedia</a>: &ldquo;The lowest common ancestor is defined between two nodes p&nbsp;and q&nbsp;as the lowest node in T that has both p&nbsp;and q&nbsp;as descendants (where we allow <b>a node to be a descendant of itself</b>).&rdquo;</p>

<p>Given the following binary tree:&nbsp; root =&nbsp;[3,5,1,6,2,0,8,null,null,7,4]</p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;" />
<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<strong>Output:</strong> 3
<strong>Explanation: </strong>The LCA of nodes <code>5</code> and <code>1</code> is <code>3.</code>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<strong>Output:</strong> 5
<strong>Explanation: </strong>The LCA of nodes <code>5</code> and <code>4</code> is <code>5</code>, since a node can be a descendant of itself according to the LCA definition.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>All of the nodes&#39; values will be unique.</li>
	<li>p and q are different and both values will&nbsp;exist in the binary tree.</li>
</ul>


-----------


## Similar Problems

- [Easy] [Lowest Common Ancestor of a Binary Search Tree](lowest-common-ancestor-of-a-binary-search-tree)




## Solution:

[TOC]

## Solution

First the given nodes `p` and `q` are to be searched in a binary tree and then their lowest common ancestor is to be found. We can resort to a normal tree traversal to search for the two nodes. Once we reach the desired nodes `p` and `q`, we can backtrack and find the lowest common ancestor.

<center>
<img src="../Figures/236/236_LCA_Binary_1.png" width="600"/>
</center>

#### Approach 1: Recursive Approach

**Intuition**

The approach is pretty intuitive. Traverse the tree in a depth first manner. The moment you encounter either of the nodes `p` or `q`, return some boolean flag. The flag helps to determine if we found the required nodes in any of the paths. The least common ancestor would then be the node for which both the subtree recursions return a `True` flag. It can also be the node which itself is one of `p` or `q` and for which one of the subtree recursions returns a `True` flag.

Let us look at the formal algorithm based on this idea.

**Algorithm**

1. Start traversing the tree from the root node.
2. If the current node itself is one of `p` or `q`, we would mark a variable `mid` as `True` and continue the search for the other node in the left and right branches.
3. If either of the left or the right branch returns `True`, this means one of the two nodes was found below.
4. If at any point in the traversal, any two of the three flags `left`, `right` or `mid` become `True`, this means we have found the lowest common ancestor for the nodes `p` and `q`.

Let us look at a sample tree and we search for the lowest common ancestor of two nodes `9` and `11` in the tree.

<center>

!?!../Documents/236_LCA_Binary_Tree_1.json:770,460!?!

</center>

Following is the sequence of nodes that are followed in the recursion:

<pre>
1 --> 2 --> 4 --> 8
BACKTRACK 8 --> 4
4 --> 9 (ONE NODE FOUND, return True)
BACKTRACK 9 --> 4 --> 2
2 --> 5 --> 10
BACKTRACK 10 --> 5
5 --> 11 (ANOTHER NODE FOUND, return True)
BACKTRACK 11 --> 5 --> 2

2 is the node where we have left = True and right = True and hence it is the lowest common ancestor.
</pre>


<iframe src="https://leetcode.com/playground/xy87wUjj/shared" frameBorder="0" width="100%" height="500" name="xy87wUjj"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.

* Space Complexity: $$O(N)$$. This is because the maximum amount of space utilized by the recursion stack would be $$N$$ since the height of a skewed binary tree could be $$N$$.
<br/>
<br/>

---

#### Approach 2: Iterative using parent pointers

**Intuition**

If we have parent pointers for each node we can traverse back from `p` and `q` to get their ancestors. The first common node we get during this traversal would be the LCA node. We can save the parent pointers in a dictionary as we traverse the tree.

**Algorithm**

1. Start from the root node and traverse the tree.
2. Until we find `p` and `q` both, keep storing the parent pointers in a dictionary.
3. Once we have found both `p` and `q`, we get all the ancestors for `p` using the parent dictionary and add to a set called `ancestors`.
4. Similarly, we traverse through ancestors for node `q`. If the ancestor is present in the ancestors set for `p`, this means this is the first ancestor common between `p` and `q` (while traversing upwards) and hence this is the LCA node.

<iframe src="https://leetcode.com/playground/CVzZroWp/shared" frameBorder="0" width="100%" height="500" name="CVzZroWp"></iframe>

**Complexity Analysis**

* Time Complexity : $$O(N)$$, where $$N$$ is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree.

* Space Complexity : $$O(N)$$. In the worst case space utilized by the stack, the parent pointer dictionary and the ancestor set, would be $$N$$ each, since the height of a skewed binary tree could be $$N$$.
<br>
<br>

---

#### Approach 3: Iterative without parent pointers

**Intuition**

In the previous approach, we come across the LCA during the backtracking process. We can get rid of the backtracking process itself. In this approach we always have a pointer to the probable LCA and the moment we find both the nodes we return the pointer as the answer.

**Algorithm**

1. Start with root node.
2. Put the `(root, root_state)` on to the stack. `root_state` defines whether one of the children or both children of `root` are left for traversal.
3. While the stack is not empty, peek into the top element of the stack represented as `(parent_node, parent_state)`.
4. Before traversing any of the child nodes of `parent_node` we check if the `parent_node` itself is one of `p` or `q`.
5. First time we find either of `p` or `q`, set a boolean flag called `one_node_found` to `True`. Also start keeping track of the lowest common ancestors by keeping a note of the top index of the stack in the variable `LCA_index`. Since all the current elements of the stack are ancestors of the node we just found.
6. The second time `parent_node == p or parent_node == q` it means we have found both the nodes and we can return the `LCA node`.
7. Whenever we visit a child of a `parent_node` we push the `(parent_node, updated_parent_state)` onto the stack. We update the state of the parent since a child/branch has been visited/processed and accordingly the state changes.
8. A node finally gets popped off from the stack when the state becomes `BOTH_DONE` implying both left and right subtrees have been pushed onto the stack and processed. If `one_node_found` is `True` then we need to check if the top node being popped could be one of the ancestors of the found node. In that case we need to reduce `LCA_index` by one. Since one of the ancestors was popped off.

> Whenever both `p` and `q` are found, `LCA_index` would be pointing to an index in the stack which would contain all the common ancestors between `p` and `q`. And the `LCA_index` element has the `lowest` ancestor common between p and q.

<center>

!?!../Documents/236_LCA_Binary_Tree_2.json:770,460!?!

</center>

The animation above shows how a stack is used to traverse the binary tree and keep track of the common ancestors between nodes `p` and `q`.

<iframe src="https://leetcode.com/playground/sFHRnjM7/shared" frameBorder="0" width="100%" height="500" name="sFHRnjM7"></iframe>

**Complexity Analysis**

* Time Complexity : $$O(N)$$, where $$N$$ is the number of nodes in the binary tree. In the worst case we might be visiting all the nodes of the binary tree. The advantage of this approach is that we can prune backtracking. We simply return once both the nodes are found.

* Space Complexity : $$O(N)$$. In the worst case the space utilized by stack would be $$N$$ since the height of a skewed binary tree could be $$N$$.

<br/>

---
Analysis written by: [@godayaldivya](https://leetcode.com/godayaldivya/). Approach 2  inspired by [@dietpepsi](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65236/JavaPython-iterative-solution).
