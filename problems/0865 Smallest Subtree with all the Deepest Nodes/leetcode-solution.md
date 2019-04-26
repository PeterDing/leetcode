# 0865 - Smallest Subtree with all the Deepest Nodes

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree | [Leetcode](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes) | [solution](https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/solution/)


-----------

<p>Given a binary tree rooted at <code>root</code>, the <em>depth</em> of each node is the shortest distance to the root.</p>

<p>A node is <em>deepest</em> if it has the largest depth possible among&nbsp;any node in the <u>entire tree</u>.</p>

<p>The subtree of a node is that node, plus the set of all descendants of that node.</p>

<p>Return the node with the largest depth such that it contains all the deepest nodes in its subtree.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,5,1,6,2,0,8,null,null,7,4]</span>
<strong>Output: </strong><span id="example-output-1">[2,7,4]</span>
<strong>Explanation:
</strong>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png" style="width: 280px; height: 238px;" />

We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input &quot;[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]&quot; is a serialization of the given tree.
The output &quot;[2, 7, 4]&quot; is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li>The number of nodes in the tree will be between 1 and 500.</li>
	<li>The values of each node are unique.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Paint Deepest Nodes

**Intuition**

We try a straightforward approach that has two phases.

The first phase is to identify the nodes of the tree that are deepest.  To do this, we have to annotate the depth of each node.  We can do this with a depth first search.

Afterwards, we will use that annotation to help us find the answer:

* If the `node` in question has maximum depth, it is the answer.

* If both the left and right child of a `node` have a deepest descendant, then the answer is this parent `node`.  

* Otherwise, if some child has a deepest descendant, then the answer is that child.

* Otherwise, the answer for this subtree doesn't exist.

**Algorithm**

In the first phase, we use a depth first search `dfs` to annotate our nodes.

In the second phase, we also use a depth first search `answer(node)`, returning the answer for the subtree at that `node`, and using the rules above to build our answer from the answers of the children of `node`.

Note that in this approach, the `answer` function returns answers that have the deepest nodes of the *entire* tree, not just the subtree being considered.

<iframe src="https://leetcode.com/playground/BShzUaRJ/shared" frameBorder="0" width="100%" height="500" name="BShzUaRJ"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the tree.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Recursion

**Intuition**

We can combine both depth first searches in *Approach #1* into an approach that does both steps in one pass.  We will have some function `dfs(node)` that returns both the answer for this subtree, and the distance from `node` to the deepest nodes in this subtree.

**Algorithm**

The `Result` (on some subtree) returned by our (depth-first search) recursion will have two parts:
* `Result.node`: the largest depth node that is equal to or an ancestor of all the deepest nodes of this subtree.
* `Result.dist`: the number of nodes in the path from the root of this subtree, to the deepest node in this subtree.

We can calculate these answers disjointly for `dfs(node)`:

* To calculate the `Result.node` of our answer:

    * If one `childResult` has deeper nodes, then `childResult.node` will be the answer.

    * If they both have the same depth nodes, then `node` will be the answer.

* The `Result.dist` of our answer is always 1 more than the largest `childResult.dist` we have.

<iframe src="https://leetcode.com/playground/QAN4y6ev/shared" frameBorder="0" width="100%" height="500" name="QAN4y6ev"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the number of nodes in the tree.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
