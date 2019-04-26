# 0797 - All Paths From Source to Target

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium |  | [Leetcode](https://leetcode.com/problems/all-paths-from-source-to-target) | [solution](https://leetcode.com/problems/all-paths-from-source-to-target/solution/)


-----------

<p>Given a directed, acyclic graph of <code>N</code> nodes.&nbsp; Find all possible paths from node <code>0</code> to node <code>N-1</code>, and return them in any order.</p>

<p>The graph is given as follows:&nbsp; the nodes are 0, 1, ..., graph.length - 1.&nbsp; graph[i] is a list of all nodes j for which the edge (i, j) exists.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> [[1,2], [3], [3], []] 
<strong>Output:</strong> [[0,1,3],[0,2,3]] 
<strong>Explanation:</strong> The graph looks like this:
0---&gt;1
|    |
v    v
2---&gt;3
There are two paths: 0 -&gt; 1 -&gt; 3 and 0 -&gt; 2 -&gt; 3.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li>The number of nodes in the graph will be in the range <code>[2, 15]</code>.</li>
	<li>You can print different paths in any order, but you should keep the order of nodes inside one path.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Recursion [Accepted]

**Intuition**

Since the graph is a directed, acyclic graph, any path from `A` to `B` is going to be composed of `A` plus a path from any neighbor of `A` to `B`.  We can use a recursion to return the answer.

**Algorithm**

Let `N` be the number of nodes in the graph.  If we are at node `N-1`, the answer is just the path `{N-1}`.  Otherwise, if we are at node `node`, the answer is `{node} + {path from nei to N-1}` for each neighbor `nei` of `node`.  This is a natural setting to use a recursion to form the answer.

<iframe src="https://leetcode.com/playground/KUaNbvp4/shared" frameBorder="0" width="100%" height="463" name="KUaNbvp4"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(2^N N^2)$$.  We can have exponentially many paths, and for each such path, our prepending operation `path.add(0, node)` will be $$O(N^2)$$.

* Space Complexity: $$O(2^N N)$$, the size of the output dominating the final space complexity.

---

Analysis written by: [@awice](https://leetcode.com/awice).
