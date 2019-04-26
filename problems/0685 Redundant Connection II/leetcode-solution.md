# 0685 - Redundant Connection II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Tree, Depth-first Search, Union Find, Graph | [Leetcode](https://leetcode.com/problems/redundant-connection-ii) | [solution](https://leetcode.com/problems/redundant-connection-ii/solution/)


-----------

<p>
In this problem, a rooted tree is a <b>directed</b> graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.
</p><p>
The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added.  The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
</p><p>
The resulting graph is given as a 2D-array of <code>edges</code>.  Each element of <code>edges</code> is a pair <code>[u, v]</code> that represents a <b>directed</b> edge connecting nodes <code>u</code> and <code>v</code>, where <code>u</code> is a parent of child <code>v</code>.
</p><p>
Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes.  If there are multiple answers, return the answer that occurs last in the given 2D-array.
</p><p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [[1,2], [1,3], [2,3]]
<b>Output:</b> [2,3]
<b>Explanation:</b> The given directed graph will be like this:
  1
 / \
v   v
2-->3
</pre>
</p>
<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [[1,2], [2,3], [3,4], [4,1], [1,5]]
<b>Output:</b> [4,1]
<b>Explanation:</b> The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3
</pre>
</p>
<p><b>Note:</b><br />
<li>The size of the input 2D-array will be between 3 and 1000.</li>
<li>Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.</li>
</p>

-----------


## Similar Problems

- [Medium] [Redundant Connection](redundant-connection)




## Solution:

[TOC]

#### Approach #1: Depth-First Search [Accepted]

**Intuition**

Starting from a rooted tree with `N-1` edges and `N` vertices, let's enumerate the possibilities for the added "redundant" edge.  If there is no loop, then either one vertex must have two parents (or no edge is redundant.)  If there is a loop, then either one vertex has two parents, or every vertex has one parent.

In the first two cases, there are only two candidates for deleting an edge, and we can try removing the last one and seeing if that works.  In the last case, the last edge of the cycle can be removed: for example, when `1->2->3->4->1->5`, we want the last edge (by order of occurrence) in the cycle `1->2->3->4->1` (but not necessarily `1->5`).

**Algorithm**

We'll first construct the underlying graph, keeping track of edges coming from nodes with multiple parents.  After, we either have 2 or 0 `candidates`.

If there are no candidates, then every vertex has one parent, such as in the case `1->2->3->4->1->5`.  From any node, we walk towards it's parent until we revisit a node - then we must be inside the cycle, and any future seen nodes are part of that cycle.  Now we take the last edge that occurs in the cycle.

Otherwise, we'll see if the graph induced by `parent` is a rooted tree.  We again take the `root` by walking from any node towards the parent until we can't, then we perform a depth-first search on this `root`.  If we visit every node, then removing the last of the two edge candidates is acceptable, and we should.  Otherwise, we should remove the first of the two edge candidates.

In our solution, we use `orbit` to find the result upon walking from a node `x` towards it's parent repeatedly until you revisit a node or can't walk anymore.  `orbit(x).node` (or `orbit(x)[0]` in Python) will be the resulting node, while `orbit(x).seen` (or `orbit(x)[1]`) will be all the nodes visited.

<iframe src="https://leetcode.com/playground/sHSf6pyj/shared" frameBorder="0" width="100%" height="500" name="sHSf6pyj"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$ where $$N$$ is the number of vertices (and also the number of edges) in the graph.  We perform a depth-first search.

* Space Complexity:  $$O(N)$$, the size of the graph.

---

Analysis written by: [@awice](https://leetcode.com/awice)
