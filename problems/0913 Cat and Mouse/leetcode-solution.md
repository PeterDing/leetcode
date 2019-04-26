# 0913 - Cat and Mouse

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Breadth-first Search, Minimax | [Leetcode](https://leetcode.com/problems/cat-and-mouse) | [solution](https://leetcode.com/problems/cat-and-mouse/solution/)


-----------

<p>A game on an <strong>undirected</strong> graph is played by two players, Mouse and Cat, who alternate turns.</p>

<p>The graph is given as follows: <code>graph[a]</code> is a list of all nodes <code>b</code> such that <code>ab</code> is an edge of the graph.</p>

<p>Mouse starts at node 1 and goes first, Cat starts at node 2 and goes second, and there is a Hole at node 0.</p>

<p>During each player&#39;s turn, they <strong>must</strong> travel along one&nbsp;edge of the graph that meets where they are.&nbsp; For example, if the Mouse is at node <code>1</code>, it <strong>must</strong> travel to any node in <code>graph[1]</code>.</p>

<p>Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)</p>

<p>Then, the game can end in 3 ways:</p>

<ul>
	<li>If ever the Cat occupies the same node as the Mouse, the Cat wins.</li>
	<li>If ever the Mouse reaches the Hole, the Mouse wins.</li>
	<li>If ever a position is repeated (ie.&nbsp;the players are in the same position as a previous turn, and&nbsp;it is the same player&#39;s turn to move), the game is a draw.</li>
</ul>

<p>Given a <code>graph</code>, and assuming both players play optimally, return <code>1</code>&nbsp;if the game is won by Mouse, <code>2</code>&nbsp;if the game is won by Cat, and <code>0</code>&nbsp;if the game is a draw.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]</span>
<strong>Output: </strong><span id="example-output-1">0
<strong>Explanation:</strong>
</span>4---3---1
|&nbsp; &nbsp;|
2---5
&nbsp;\&nbsp;/
&nbsp; 0
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>3 &lt;= graph.length &lt;= 50</code></li>
	<li>It is guaranteed that <code>graph[1]</code> is non-empty.</li>
	<li>It is guaranteed that <code>graph[2]</code> contains a non-zero element.&nbsp;</li>
</ol>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Minimax / Percolate from Resolved States

**Intuition**

The state of the game can be represented as `(m, c, t)` where `m` is the location of the mouse, `c` is the location of the cat, and `t` is `1` if it is the mouse's move, else `2`.  Let's call these states *nodes*.  These states form a directed graph: the player whose turn it is has various moves which can be considered as outgoing edges from this node to other nodes.

Some of these nodes are already resolved: if the mouse is at the hole `(m = 0)`, then the mouse wins; if the cat is where the mouse is `(c = m)`, then the cat wins.  Let's say that nodes will either be colored $$\small\text{MOUSE}$$, $$\small\text{CAT}$$, or $$\small\text{DRAW}$$ depending on which player is assured victory.

As in a standard minimax algorithm, the Mouse player will prefer $$\small\text{MOUSE}$$ nodes first, $$\small\text{DRAW}$$ nodes second, and $$\small\text{CAT}$$ nodes last, and the Cat player prefers these nodes in the opposite order.

**Algorithm**

We will color each `node` marked $$\small\text{DRAW}$$ according to the following rule.  (We'll suppose the `node` has `node.turn = Mouse`: the other case is similar.)

* ("Immediate coloring"):  If there is a child that is colored $$\small\text{MOUSE}$$, then this node will also be colored $$\small\text{MOUSE}$$.

* ("Eventual coloring"):  If all children are colored $$\small\text{CAT}$$, then this node will also be colored $$\small\text{CAT}$$.

We will repeatedly do this kind of coloring until no `node` satisfies the above conditions.  To perform this coloring efficiently, we will use a queue and perform a *bottom-up percolation*:

* Enqueue any node initially colored (because the Mouse is at the Hole, or the Cat is at the Mouse.)

* For every `node` in the queue, for each `parent` of that `node`:

  * Do an immediate coloring of `parent` if you can.

  * If you can't, then decrement the side-count of the number of children marked $$\small\text{DRAW}$$.  If it becomes zero, then do an "eventual coloring" of this parent.

  * All `parents` that were colored in this manner get enqueued to the queue.

**Proof of Correctness**

Our proof is similar to a proof that minimax works.

Say we cannot color any nodes any more, and say from any node colored $$\small\text{CAT}$$ or $$\small\text{MOUSE}$$ we need at most $$K$$ moves to win.  If say, some node marked $$\small\text{DRAW}$$ is actually a win for Mouse, it must have been with $$> K$$ moves.  Then, a path along optimal play (that tries to prolong the loss as long as possible) must arrive at a node colored $$\small\text{MOUSE}$$ (as eventually the Mouse reaches the Hole.)  Thus, there must have been some transition $$\small\text{DRAW} \rightarrow \small\text{MOUSE}$$ along this path.

If this transition occurred at a `node` with `node.turn = Mouse`, then it breaks our immediate coloring rule.  If it occured with `node.turn = Cat`, and all children of `node` have color $$\small\text{MOUSE}$$, then it breaks our eventual coloring rule.  If some child has color $$\small\text{CAT}$$, then it breaks our immediate coloring rule.  Thus, in this case `node` will have some child with $$\small\text{DRAW}$$, which breaks our optimal play assumption, as moving to this child ends the game in $$> K$$ moves, whereas moving to the colored neighbor ends the game in $$\leq K$$ moves.

<iframe src="https://leetcode.com/playground/sEZarXgw/shared" frameBorder="0" width="100%" height="500" name="sEZarXgw"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^3)$$, where $$N$$ is the number of nodes in the graph.  There are $$O(N^2)$$ states, and each state has an outdegree of $$N$$, as there are at most $$N$$ different moves.

* Space Complexity:  $$O(N^2)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
