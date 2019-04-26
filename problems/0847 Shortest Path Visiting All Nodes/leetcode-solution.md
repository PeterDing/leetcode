# 0847 - Shortest Path Visiting All Nodes

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming, Breadth-first Search | [Leetcode](https://leetcode.com/problems/shortest-path-visiting-all-nodes) | [solution](https://leetcode.com/problems/shortest-path-visiting-all-nodes/solution/)


-----------

<p>An undirected, connected graph of N nodes (labeled&nbsp;<code>0, 1, 2, ..., N-1</code>) is given as <code>graph</code>.</p>

<p><code>graph.length = N</code>, and <code>j != i</code>&nbsp;is in the list&nbsp;<code>graph[i]</code>&nbsp;exactly once, if and only if nodes <code>i</code> and <code>j</code> are connected.</p>

<p>Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[[1,2,3],[0],[0],[0]]
<strong>Output: </strong>4
<strong>Explanation</strong>: One possible path is [1,0,2,0,3]</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[[1],[0,2,4],[1,3,4],[2],[1,2]]
<strong>Output: </strong>4
<strong>Explanation</strong>: One possible path is [0,1,4,2,3]
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= graph.length &lt;= 12</code></li>
	<li><code>0 &lt;= graph[i].length &lt;&nbsp;graph.length</code></li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Breadth First Search [Accepted]

**Intuition**

A path 'state' can be represented as the subset of nodes visited, plus the current 'head' node.  Then, the problem reduces to a shortest path problem among these states, which can be solved with a breadth-first search.

**Algorithm**

Let's call the set of nodes visited by a path so far the *cover*, and the current node as the *head*.  We'll store the `cover` states using set bits: `k` is in the cover if the `k`th bit of `cover` is 1.

For states `state = (cover, head)`, we can perform a breadth-first search on these states.  The neighbors are `(cover | (1 << child), child)` for each `child in graph[head]`.

If at any point we find a state with all set bits in it's cover, because it is a breadth-first search, we know this must represent the shortest path length.

<iframe src="https://leetcode.com/playground/RSKL3uRn/shared" frameBorder="0" width="100%" height="500" name="RSKL3uRn"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(2^N * N)$$.

* Space Complexity:  $$O(2^N * N)$$.

---
#### Approach #2: Dynamic Programming [Accepted]

**Intuition**

A path 'state' can be represented as the subset of nodes visited, plus the current 'head' node.  As in Approach #1, we have a recurrence in states: `answer(cover, head)` is `min(1 + answer(cover | (1<<child), child) for child in graph[head])`.  Because these states form a DAG (a directed graph with no cycles), we can do dynamic programming.

**Algorithm**

Let's call the set of nodes visited by a path so far the *cover*, and the current node as the *head*.  We'll store `dist[cover][head]` as the length of the shortest path with that cover and head.  We'll store the `cover` states using set bits, and maintain the loop invariant (on `cover`), that `dist[k][...]` is correct for `k < cover`.

For every state `(cover, head)`, the possible `next` (neighbor) nodes in the path are found in `graph[head]`.  The new `cover2` is the old cover plus `next`.

For each of these, we perform a "relaxation step" (for those familiar with the Bellman-Ford algorithm), where if the new candidate distance for `dist[cover2][next]` is larger than `dist[cover][head] + 1`, we'll update it to `dist[cover][head] + 1`.

Care must be taken to perform the relaxation step multiple times on the same cover if `cover = cover2`.  This is because a minimum state for `dist[cover][head]` might only be achieved through multiple steps through some path.

Finally, it should be noted that we are using implicitly the fact that when iterating `cover = 0 .. (1<<N) - 1`, that each new cover `cover2 = cover | 1 << x` is such that `cover2 >= cover`.  This implies a topological ordering, which means that the recurrence on these states form a DAG.

<iframe src="https://leetcode.com/playground/f8jJAcDL/shared" frameBorder="0" width="100%" height="500" name="f8jJAcDL"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(2^N * N)$$.

* Space Complexity:  $$O(2^N * N)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
