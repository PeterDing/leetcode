# 0743 - Network Delay Time

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Heap, Depth-first Search, Breadth-first Search, Graph | [Leetcode](https://leetcode.com/problems/network-delay-time) | [solution](https://leetcode.com/problems/network-delay-time/solution/)


-----------

<p>There are <code>N</code> network nodes, labelled <code>1</code> to <code>N</code>.</p>

<p>Given <code>times</code>, a list of travel times as <b>directed</b> edges <code>times[i] = (u, v, w)</code>, where <code>u</code> is the source node, <code>v</code> is the target node, and <code>w</code> is the time it takes for a signal to travel from source to target.</p>

<p>Now, we send a signal from a certain node <code>K</code>. How long will it take for all nodes to receive the signal? If it is impossible, return <code>-1</code>.</p>

<p><b>Note:</b></p>

<ol>
	<li><code>N</code> will be in the range <code>[1, 100]</code>.</li>
	<li><code>K</code> will be in the range <code>[1, N]</code>.</li>
	<li>The length of <code>times</code> will be in the range <code>[1, 6000]</code>.</li>
	<li>All edges <code>times[i] = (u, v, w)</code> will have <code>1 &lt;= u, v &lt;= N</code> and <code>0 &lt;= w &lt;= 100</code>.</li>
</ol>

<p>&nbsp;</p>


-----------


## Similar Problems




## Solution:

[TOC]

#### Approach #1: Depth-First Search [Accepted]

**Intuition**

Let's record the time `dist[node]` when the signal reaches the node.  If some signal arrived earlier, we don't need to broadcast it anymore.  Otherwise, we should broadcast the signal.

**Algorithm**

We'll maintain `dist[node]`, the earliest that we arrived at each `node`.  When visiting a `node` while `elapsed` time has elapsed, if this is the currently-fastest signal at this node, let's broadcast signals from this node.

To speed things up, at each visited node we'll consider signals exiting the node that are faster first, by sorting the edges.


<iframe src="https://leetcode.com/playground/YadsYraY/shared" frameBorder="0" width="100%" height="500" name="YadsYraY"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^N + E \log E)$$ where $$E$$ is the length of `times`.  We can only fully visit each node up to $$N-1$$ times, one per each other node.  Plus, we have to explore every edge and sort them.  Sorting each small bucket of outgoing edges is bounded by sorting all of them, because of repeated use of the inequality $$x \log x + y \log y \leq (x+y) \log (x+y)$$.

* Space Complexity: $$O(N + E)$$, the size of the graph ($$O(E)$$), plus the size of the implicit call stack in our DFS ($$O(N)$$).

---
#### Approach #2: Dijkstra's Algorithm [Accepted]

**Intuition and Algorithm**

We use *Dijkstra's algorithm* to find the shortest path from our source to all targets.  This is a textbook algorithm, refer to [this link](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) for more details.

Dijkstra's algorithm is based on repeatedly making the candidate move that has the least distance travelled.

In our implementations below, we showcase both $$O(N^2)$$ (basic) and $$O(N \log N)$$ (heap) approaches.

*Basic Implementation*
<iframe src="https://leetcode.com/playground/HxrhmhUo/shared" frameBorder="0" width="100%" height="500" name="HxrhmhUo"></iframe>

*Heap Implementation*

<iframe src="https://leetcode.com/playground/FAHPcmsE/shared" frameBorder="0" width="100%" height="500" name="FAHPcmsE"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^2 + E)$$m where $$E$$ is the length of `times` in the basic implementation, and $$O(E \log E)$$ in the heap implementation, as potentially every edge gets added to the heap.

* Space Complexity: $$O(N + E)$$, the size of the graph ($$O(E)$$), plus the size of the other objects used ($$O(N)$$).

---

Analysis written by: [@awice](https://leetcode.com/awice).
