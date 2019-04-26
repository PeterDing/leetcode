# 0684 - Redundant Connection

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Tree, Union Find, Graph | [Leetcode](https://leetcode.com/problems/redundant-connection) | [solution](https://leetcode.com/problems/redundant-connection/solution/)


-----------

<p>
In this problem, a tree is an <b>undirected</b> graph that is connected and has no cycles.
</p><p>
The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added.  The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
</p><p>
The resulting graph is given as a 2D-array of <code>edges</code>.  Each element of <code>edges</code> is a pair <code>[u, v]</code> with <code>u < v</code>, that represents an <b>undirected</b> edge connecting nodes <code>u</code> and <code>v</code>.
</p><p>
Return an edge that can be removed so that the resulting graph is a tree of N nodes.  If there are multiple answers, return the answer that occurs last in the given 2D-array.  The answer edge <code>[u, v]</code> should be in the same format, with <code>u < v</code>.
</p><p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [[1,2], [1,3], [2,3]]
<b>Output:</b> [2,3]
<b>Explanation:</b> The given undirected graph will be like this:
  1
 / \
2 - 3
</pre>
</p>
<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [[1,2], [2,3], [3,4], [1,4], [1,5]]
<b>Output:</b> [1,4]
<b>Explanation:</b> The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
</pre>
</p>
<p><b>Note:</b><br />
<li>The size of the input 2D-array will be between 3 and 1000.</li>
<li>Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.</li>
</p>

<br />

<p>
<b><font color="red">Update (2017-09-26):</font></b><br>
We have overhauled the problem description + test cases and specified clearly the graph is an <b><i>undirected</i></b> graph. For the <b><i>directed</i></b> graph follow up please see <b><a href="https://leetcode.com/problems/redundant-connection-ii/description/">Redundant Connection II</a></b>). We apologize for any inconvenience caused.
</p>

-----------


## Similar Problems

- [Hard] [Redundant Connection II](redundant-connection-ii)

- [Medium] [Accounts Merge](accounts-merge)




## Solution:

[TOC]

#### Approach #1: DFS [Accepted]

**Intuition and Algorithm**

For each edge `(u, v)`, traverse the graph with a depth-first search to see if we can connect `u` to `v`.  If we can, then it must be the duplicate edge.

<iframe src="https://leetcode.com/playground/W7EXu5ND/shared" frameBorder="0" name="W7EXu5ND" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$ where $$N$$ is the number of vertices (and also the number of edges) in the graph.  In the worst case, for every edge we include, we have to search every previously-occurring edge of the graph.

* Space Complexity:  $$O(N)$$.  The current construction of the graph has at most $$N$$ nodes.

---
#### Approach #2: Union-Find [Accepted]

**Intuition and Algorithm**

If we are familiar with a Disjoint Set Union (DSU) data structure, we can use this in a straightforward manner to solve the problem: we simply find the first edge occurring in the graph that is already connected.  The rest of this explanation will focus on the details of implementing DSU.

A DSU data structure can be used to maintain knowledge of the connected components of a graph, and query for them quickly.  In particular, we would like to support two operations:

* `dsu.find(node x)`, which outputs a unique id so that two nodes have the same id if and only if they are in the same connected component, and:

* `dsu.union(node x, node y)`, which draws an edge `(x, y)` in the graph, connecting the components with id `find(x)` and `find(y)` together.

To achieve this, we keep track of `parent`, which remembers the `id` of a smaller node in the same connected component.  If the node is it's own parent, we call this the *leader* of that connected component.

A naive implementation of a DSU structure would look something like this:

*Psuedocode*

<iframe src="https://leetcode.com/playground/sCjT3wyq/shared" frameBorder="0" name="sCjT3wyq" width="100%" height="190"></iframe>

We use two techniques to improve the run-time complexity: *path compression*, and *union-by-rank*.

* Path compression involves changing the `x = parent[x]` in the `find` function to `parent[x] = find(parent[x])`.  Basically, as we compute the correct leader for x, we should remember our calculation.

* Union-by-rank involves distributing the workload of `find` across leaders evenly.  Whenever we `dsu.union(x, y)`, we have two leaders `xr, yr` and we have to choose whether we want `parent[x] = yr` or `parent[y] = xr`.  We choose the leader that has a higher following to pick up a new follower.  
Specifically, the meaning of `rank` is that there are less than `2 ^ rank[x]` followers of `x`.  This strategy can be shown to give us better bounds for how long the recursive loop in `dsu.find` could run for.

<iframe src="https://leetcode.com/playground/tFfjEuXo/shared" frameBorder="0" name="tFfjEuXo" width="100%" height="515"></iframe>

*Alternate Implementation of DSU without Union-By-Rank*
<iframe src="https://leetcode.com/playground/DzMVxYRc/shared" frameBorder="0" name="DzMVxYRc" width="100%" height="207"></iframe>

<iframe src="https://leetcode.com/playground/YgdvM9bJ/shared" frameBorder="0" name="YgdvM9bJ" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N\alpha(N)) \approx O(N)$$, where $$N$$ is the number of vertices (and also the number of edges) in the graph, and $$\alpha$$ is the *Inverse-Ackermann* function.  We make up to $$N$$ queries of `dsu.union`, which takes (amortized) $$O(\alpha(N))$$ time.  Outside the scope of this article, it can be shown why `dsu.union` has $$O(\alpha(N))$$ complexity, what the Inverse-Ackermann function is, and why $$O(\alpha(N))$$ is approximately $$O(1)$$.

* Space Complexity:  $$O(N)$$.  The current construction of the graph (embedded in our `dsu` structure) has at most $$N$$ nodes.

---

Analysis written by: [@awice](https://leetcode.com/awice)
