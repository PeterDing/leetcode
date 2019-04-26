# 0854 - K-Similar Strings

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Breadth-first Search, Graph | [Leetcode](https://leetcode.com/problems/k-similar-strings) | [solution](https://leetcode.com/problems/k-similar-strings/solution/)


-----------

<p>Strings&nbsp;<code>A</code> and <code>B</code> are <code>K</code>-similar (for some non-negative integer <code>K</code>) if we can swap the positions of two letters in <code>A</code> exactly <code>K</code>&nbsp;times so that the resulting string equals <code>B</code>.</p>

<p>Given two anagrams <code>A</code> and <code>B</code>, return the smallest <code>K</code>&nbsp;for which <code>A</code> and <code>B</code> are <code>K</code>-similar.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">&quot;ab&quot;</span>, B = <span id="example-input-1-2">&quot;ba&quot;</span>
<strong>Output: </strong><span id="example-output-1">1</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">&quot;abc&quot;</span>, B = <span id="example-input-2-2">&quot;bca&quot;</span>
<strong>Output: </strong><span id="example-output-2">2</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">&quot;abac&quot;</span>, B = <span id="example-input-3-2">&quot;baca&quot;</span>
<strong>Output: </strong><span id="example-output-3">2</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-4-1">&quot;aabc&quot;</span>, B = <span id="example-input-4-2">&quot;abca&quot;</span>
<strong>Output: </strong><span id="example-output-4">2</span></pre>
</div>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length == B.length &lt;= 20</code></li>
	<li><code>A</code> and <code>B</code> contain only lowercase letters from the set <code>{&#39;a&#39;, &#39;b&#39;, &#39;c&#39;, &#39;d&#39;, &#39;e&#39;, &#39;f&#39;}</code></li>
</ol>


-----------


## Similar Problems

- [Hard] [Couples Holding Hands](couples-holding-hands)




## Solution:

[TOC]

## Solution
---
#### Approach Framework

**Explanation**

We'll call the *underlying graph* of the problem, the graph with 6 nodes `'a', 'b', ..., 'f'` and the edges `A[i] -> B[i]`.  Our goal is for this graph to have only self-edges (edges of the form `a -> a`.)  Let's make some deductions about how swaps between `A[i]` and `A[j]` affect this graph, and the nature of optimal swap schedules.

If `A = 'ca...'` and `B = 'ab...'`, then the first two edges of the underlying graph are `c -> a` and `a -> b`; and a swap between `A[1]` and `A[0]` changes these two edges to the single edge `c -> b`.  Let's call this type of operation *'cutting corners'*.  Intuitively, our optimal swap schedule always increases the number of matches (`A[i] == B[i]`s) for each swap, so cutting corners is the only type of operation we need to consider.  (This is essentially the *happy swap assumption*, proved in [765 - Couples Holding Hands](https://leetcode.com/articles/couples-holding-hands/))

Now consider any cycle decomposition of the underlying graph.  [This decomposition (or the number of cycles), is not necessarily unique.]  Through operations of cutting corners, we'll delete all the (non-self) edges.  Each cycle of length `k` requires `k-1` operations to delete.  Thus, the answer is just the minimum possible value of $$\sum (C_k - 1)$$, where $$C_1, \cdots C_k$$ are the lengths of the cycles in some cycle decomposition of the underlying graph.  This can be re-written as $$\text{(Number of non-self edges)} - \text{(Number of cycles)}$$.  Hence, we want to maximize the number of cycles in a cycle decomposition of the underlying graph.
<br />
<br />

---

#### Approach 1: Brute Force with Dynamic Programming

**Intuition and Algorithm**

Let $$P_1, P_2, \cdots$$ be possible cycles of the underlying graph $$G$$.  Let's attempt to write $$G = \sum k_i P_i$$ for some constants $$k_i$$.  Then, the number of cycles is $$\sum k_i$$.

We can represent $$G$$ and $$P_i$$ as the number of directed edges from node $$X$$ to $$Y$$.  For example, if $$P_1$$ is the cycle `a -> b -> d -> e -> a`, then $$P_1$$ is `a -> b` plus `b -> d` plus `d -> e` plus `e -> a`.  This can be represented as a column vector `possibles[0]` of 1s and 0s, with four 1s, (each `possibles[0][i] == 1` represents the `i`th directed edge being there [and having quantity 1]).  Similarly, the graph $$G$$ can also be represented as a column vector.

This sets the stage for dynamic programming.  For each graph $$G$$, represented as a column vector, say we want to find `numCycles(G)`.  We can take all possible cycles $$C$$, and check if $$G$$ contains $$C$$.  If it does, then a candidate answer is `1 + numCycles(G - C)`.

It should also be noted that maximizing the number of cycles cannot be done in a greedy way, ie. by always removing the lowest size cycle.  For example, consider the graph with edges `a -> b -> c -> a`, `b -> d -> e -> b`, and `c -> e -> f -> c`.  Those form cycles, and there is a fourth 3-cycle `b -> c -> e -> b`.  If we remove that cycle first, then we would have only two cycles; but if we remove the first 3 cycles, then we would have three cycles.

<iframe src="https://leetcode.com/playground/FcbDkuSz/shared" frameBorder="0" width="100%" height="500" name="FcbDkuSz"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(2^{N+W})$$, where $$N$$ is the length of the string, and $$W$$ is the length of the alphabet.

* Space Complexity:  $$O(2^{N+W})$$.
<br />
<br />

---
#### Approach 2: Pruned Breadth First Search

**Intuition**

Based on the *underlying graph* interpretation of the problem, we can prove that an optimal solution swaps the left-most unmatched character `A[i]` with an appropriate match `A[j] == B[i] (j > i)`.

This reduces the number of "neighbors" of a node (string state) from $$O(N^2)$$ to $$O(N)$$, but it also focuses our search greatly.  Each node searched with `k` matches, will have at most $$2^k$$ swaps on the unmatched characters.  This leads to $$\sum_k \binom{N}{k} 2^k = 3^N$$ checked states.  Furthermore, some characters are the same, so we must divide the number of states by approximate factors of $$\prod (N_i)!$$ [where $$N_i$$ is the number of occurrences of the $$i$$th character in `A`.]  With $$N \leq 20$$, this means the number of states will be small.

**Algorithm**

We'll perform a regular breadth-first search.  The neighbors to each node string `S` are all the strings reachable with 1 swap, that match the first unmatched character in `S`.

<iframe src="https://leetcode.com/playground/nNLRdQYX/shared" frameBorder="0" width="100%" height="500" name="nNLRdQYX"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\sum_{k=0}^n \binom{N}{k} \frac{\min(2^k, (N-k)!)}{W * (\frac{N-k}{W})!})$$, where $$N$$ is the length of the string, and $$W$$ is the length of the alphabet.

* Space Complexity:  $$O(N * t)$$, where $$t$$ is the time complexity given above.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
