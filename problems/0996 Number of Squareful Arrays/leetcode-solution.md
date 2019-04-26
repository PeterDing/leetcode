# 0996 - Number of Squareful Arrays

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Math, Backtracking, Graph | [Leetcode](https://leetcode.com/problems/number-of-squareful-arrays) | [solution](https://leetcode.com/problems/number-of-squareful-arrays/solution/)


-----------

<p>Given an array <code>A</code> of non-negative integers, the array is <em>squareful</em> if for every pair of adjacent elements, their sum is a perfect square.</p>

<p>Return the number of permutations of A that are squareful.&nbsp; Two permutations <code>A1</code> and <code>A2</code> differ if and only if there is some index <code>i</code> such that <code>A1[i] != A2[i]</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,17,8]</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>
[1,8,17] and [17,8,1] are the valid permutations.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[2,2,2]</span>
<strong>Output: </strong><span id="example-output-2">1</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 12</code></li>
	<li><code>0 &lt;= A[i] &lt;= 1e9</code></li>
</ol>

-----------


## Similar Problems

- [Medium] [Permutations II](permutations-ii)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Backtracking

**Intuition**

Construct a graph where an edge from $$i$$ to $$j$$ exists if $$A[i] + A[j]$$ is a perfect square.  Our goal is to investigate Hamiltonian paths of this graph: paths that visit all the nodes exactly once.

**Algorithm**

Let's keep a current `count` of what values of nodes are left to visit, and a count `todo` of how many nodes left to visit.

From each node, we can explore all neighboring nodes (by value, which reduces the complexity blowup).

Please see the inline comments for more details.

<iframe src="https://leetcode.com/playground/bQrNAHHo/shared" frameBorder="0" width="100%" height="500" name="bQrNAHHo"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^N)$$, where $$N$$ is length of `A`.  A tighter bound is outside the scope of this article.  However, it can be shown that the underlying graph is triangle free, as well as other properties that would dramatically shrink this complexity.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Dynamic Programming

**Intuition**

As in *Approach 1*, construct an underlying graph.  Since the number of nodes is small, we can use dynamic programming with a 'visited' mask.

**Algorithm**

We construct the graph in the same method as in *Approach 1*.

Now, let `dfs(node, visited)` be the number of ways from `node` to visit the remaining unvisited nodes.  Here, `visited` is a mask: `(visited >> i) & 1` is true if and only if the `i`th node has been visited.

Afterwards, we may have overcounted if there are repeated values in `A`.  To account for this, for every `x` in `A`, if `A` contains `x` a total of `k` times, we divide the answer by `k!`.

<iframe src="https://leetcode.com/playground/odBEReYN/shared" frameBorder="0" width="100%" height="500" name="odBEReYN"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N 2^N)$$, where $$N$$ is length of `A`.

* Space Complexity:  $$O(N 2^N)$$.
<br />
<br />


Analysis written by: [@awice](https://leetcode.com/awice).
