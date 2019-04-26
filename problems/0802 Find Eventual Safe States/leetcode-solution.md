# 0802 - Find Eventual Safe States

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Depth-first Search, Graph | [Leetcode](https://leetcode.com/problems/find-eventual-safe-states) | [solution](https://leetcode.com/problems/find-eventual-safe-states/solution/)


-----------

<p>In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.&nbsp; If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.</p>

<p>Now, say our starting node is <em>eventually safe&nbsp;</em>if and only if we must eventually walk to a terminal node.&nbsp; More specifically, there exists a natural number <code>K</code> so that for any choice of where to walk, we must have stopped at a terminal node in less than <code>K</code> steps.</p>

<p>Which nodes are eventually safe?&nbsp; Return them as an array in sorted order.</p>

<p>The directed graph has <code>N</code> nodes with labels <code>0, 1, ..., N-1</code>, where <code>N</code> is the length of <code>graph</code>.&nbsp; The&nbsp;graph is given in the following form: <code>graph[i]</code> is a list of labels <code>j</code> such that <code>(i, j)</code> is a directed edge of the graph.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> graph = [[1,2],[2,3],[5],[0],[5],[],[]]
<strong>Output:</strong> [2,4,5,6]
Here is a diagram of the above graph.

</pre>

<p><img alt="Illustration of graph" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/17/picture1.png" style="height:86px; width:300px" /></p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>graph</code> will have length at most <code>10000</code>.</li>
	<li>The number of edges in the graph will not exceed <code>32000</code>.</li>
	<li>Each <code>graph[i]</code> will be a sorted list of different integers, chosen within the range <code>[0, graph.length - 1]</code>.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Reverse Edges [Accepted]

**Intuition**

The crux of the problem is whether you can reach a cycle from the node you start in.  If you can, then there is a way to avoid stopping indefinitely; and if you can't, then after some finite number of steps you'll stop.

Thinking about this property more, a node is eventually safe if all it's outgoing edges are to nodes that are eventually safe.

This gives us the following idea: we start with nodes that have no outgoing edges - those are eventually safe.  Now, we can update any nodes which only point to eventually safe nodes - those are also eventually safe.  Then, we can update again, and so on.

However, we'll need a good algorithm to make sure our updates are efficient.

**Algorithm**

We'll keep track of `graph`, a way to know for some node `i`, what the outgoing edges `(i, j)` are.  We'll also keep track of `rgraph`, a way to know for some node `j`, what the incoming edges `(i, j)` are.

Now for every node `j` which was declared eventually safe, we'll process them in a queue.  We'll look at all parents `i = rgraph[j]` and remove the edge `(i, j)` from the graph (from `graph`).  If this causes the `graph` to have no outgoing edges `graph[i]`, then we'll declare it eventually safe and add it to our queue.

Also, we'll keep track of everything we ever added to the queue, so we can read off the answer in sorted order later.

<iframe src="https://leetcode.com/playground/x49F98kC/shared" frameBorder="0" width="100%" height="500" name="x49F98kC"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N + E)$$, where $$N$$ is the number of nodes in the given graph, and $$E$$ is the total number of edges.

* Space Complexity: $$O(N)$$ in additional space complexity.


---
#### Approach #2: Depth-First Search [Accepted]

**Intuition**

As in *Approach #1*, the crux of the problem is whether you reach a cycle or not.

Let us perform a "brute force": a cycle-finding DFS algorithm on each node individually.  This is a classic "white-gray-black" DFS algorithm that would be part of any textbook on DFS.  We mark a node gray on entry, and black on exit.  If we see a gray node during our DFS, it must be part of a cycle.  In a naive view, we'll clear the colors between each search.

**Algorithm**

We can improve this approach, by noticing that we don't need to clear the colors between each search.

When we visit a node, the only possibilities are that we've marked the entire subtree black (which must be eventually safe), or it has a cycle and we have only marked the members of that cycle gray.  So indeed, the invariant that gray nodes are always part of a cycle, and black nodes are always eventually safe is maintained.

In order to exit our search quickly when we find a cycle (and not paint other nodes erroneously), we'll say the result of visiting a node is `true` if it is eventually safe, otherwise `false`.  This allows information that we've reached a cycle to propagate up the call stack so that we can terminate our search early.

<iframe src="https://leetcode.com/playground/VxkXPWTw/shared" frameBorder="0" width="100%" height="500" name="VxkXPWTw"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N + E)$$, where $$N$$ is the number of nodes in the given graph, and $$E$$ is the total number of edges.

* Space Complexity: $$O(N)$$ in additional space complexity.

---

Analysis written by: [@awice](https://leetcode.com/awice).
