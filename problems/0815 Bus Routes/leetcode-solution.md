# 0815 - Bus Routes

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Breadth-first Search | [Leetcode](https://leetcode.com/problems/bus-routes) | [solution](https://leetcode.com/problems/bus-routes/solution/)


-----------

<p>We have a list of bus routes. Each <code>routes[i]</code> is a bus route that the i-th bus&nbsp;repeats forever. For example if <code>routes[0] = [1, 5, 7]</code>, this means that the first&nbsp;bus (0-th indexed) travels in the sequence 1-&gt;5-&gt;7-&gt;1-&gt;5-&gt;7-&gt;1-&gt;... forever.</p>

<p>We start at bus stop <code>S</code> (initially not on a bus), and we want to go to bus stop <code>T</code>. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
</pre>

<p><strong>Note: </strong></p>

<ul>
	<li><code>1 &lt;= routes.length &lt;= 500</code>.</li>
	<li><code>1 &lt;= routes[i].length &lt;= 500</code>.</li>
	<li><code>0 &lt;= routes[i][j] &lt; 10 ^ 6</code>.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Breadth First Search [Accepted]

**Intuition**

Instead of thinking of the stops as nodes (of a graph), think of the buses as nodes.  We want to take the least number of buses, which is a shortest path problem, conducive to using a breadth-first search.

**Algorithm**

We perform a breadth first search on bus numbers.  When we start at `S`, originally we might be able to board many buses, and if we end at `T` we may have many `targets` for our goal state.

One difficulty is to efficiently decide whether two buses are connected by an edge.  They are connected if they share at least one bus stop.  Whether two lists share a common value can be done by set intersection (HashSet), or by sorting each list and using a two pointer approach.

To make our search easy, we will annotate the depth of each node: `info[0] = node, info[1] = depth`.

<iframe src="https://leetcode.com/playground/fji6uJ5m/shared" frameBorder="0" width="100%" height="500" name="fji6uJ5m"></iframe>

**Complexity Analysis**

* Time Complexity:  Let $$N$$ denote the number of buses, and $$b_i$$ be the number of stops on the $$i$$th bus.

    * To create the graph, in Python we do $$O(\sum (N - i) b_i)$$ work (we can improve this by checking for which of `r1, r2` is smaller), while in Java we did a $$O(\sum b_i \log b_i)$$ sorting step, plus our searches are $$O(N \sum b_i)$$ work.

    * Our (breadth-first) search is on $$N$$ nodes, and each node could have $$N$$ edges, so it is $$O(N^2)$$.

* Space Complexity: $$O(N^2 + \sum b_i)$$ additional space complexity, the size of `graph` and `routes`.  In Java, our space complexity is $$O(N^2)$$ because we do not have an equivalent of `routes`.  Dual-pivot quicksort (as used in `Arrays.sort(int[])`) is an in-place algorithm, so in Java we did not increase our space complexity by sorting.

---

Analysis written by: [@awice](https://leetcode.com/awice).
