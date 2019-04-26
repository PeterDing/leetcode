# 0873 - Length of Longest Fibonacci Subsequence

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Dynamic Programming | [Leetcode](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence) | [solution](https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/solution/)


-----------

<p>A sequence <code>X_1, X_2, ..., X_n</code>&nbsp;is <em>fibonacci-like</em> if:</p>

<ul>
	<li><code>n &gt;= 3</code></li>
	<li><code>X_i + X_{i+1} = X_{i+2}</code>&nbsp;for all&nbsp;<code>i + 2 &lt;= n</code></li>
</ul>

<p>Given a <b>strictly increasing</b>&nbsp;array&nbsp;<code>A</code> of positive integers forming a sequence, find the <strong>length</strong> of the longest fibonacci-like subsequence of <code>A</code>.&nbsp; If one does not exist, return 0.</p>

<p>(<em>Recall that a subsequence is derived from another sequence <code>A</code> by&nbsp;deleting any number of&nbsp;elements (including none)&nbsp;from <code>A</code>, without changing the order of the remaining elements.&nbsp; For example, <code>[3, 5, 8]</code> is a subsequence of <code>[3, 4, 5, 6, 7, 8]</code>.</em>)</p>

<p>&nbsp;</p>

<ul>
</ul>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[1,2,3,4,5,6,7,8]
<strong>Output: </strong>5
<strong>Explanation:
</strong>The longest subsequence that is fibonacci-like: [1,2,3,5,8].
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[1,3,7,11,12,14,18]
<strong>Output: </strong>3
<strong>Explanation</strong>:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>3 &lt;= A.length &lt;= 1000</code></li>
	<li><code>1 &lt;= A[0] &lt; A[1] &lt; ... &lt; A[A.length - 1] &lt;= 10^9</code></li>
	<li><em>(The time limit has been reduced by 50% for submissions in Java, C, and C++.)</em></li>
</ul>


-----------


## Similar Problems

- [Easy] [Fibonacci Number](fibonacci-number)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Brute Force with Set

**Intuition**

Every Fibonacci-like subsequence has each two adjacent terms determine the next expected term.  For example, with `2, 5`, we expect that the sequence must continue `7, 12, 19, 31`, etc.

We can use a `Set` structure to determine quickly whether the next term is in the array `A` or not.  Because of the exponential growth of these terms, there are at most 43 terms in any Fibonacci-like subsequence that has maximum value $$\leq 10^9$$.

**Algorithm**

For each starting pair `A[i], A[j]`, we maintain the next expected value `y = A[i] + A[j]` and the previously seen largest value `x = A[j]`.  If `y` is in the array, then we can then update these values `(x, y) -> (y, x+y)`.

Also, because subsequences are only fibonacci-like if they have length 3 or more, we must perform the check `ans >= 3 ? ans : 0` at the end.

<iframe src="https://leetcode.com/playground/HWTGNbV2/shared" frameBorder="0" width="100%" height="500" name="HWTGNbV2"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2 \log M)$$, where $$N$$ is the length of `A`, and $$M$$ is the maximum value of `A`.

* Space Complexity:  $$O(N)$$, the space used by the set `S`.
<br />
<br />


---
#### Approach 2: Dynamic Programming

**Intuition**

Think of two consecutive terms `A[i], A[j]` in a fibonacci-like subsequence as a single node `(i, j)`, and the entire subsequence is a path between these consecutive nodes.  For example, with the fibonacci-like subsequence `(A[1] = 2, A[2] = 3, A[4] = 5, A[7] = 8, A[10] = 13)`, we have the path between nodes `(1, 2) <-> (2, 4) <-> (4, 7) <-> (7, 10)`.

The motivation for this is that two nodes `(i, j)` and `(j, k)` are connected if and only if `A[i] + A[j] == A[k]`, and we needed this amount of information to know about this connection.  Now we have a problem similar to *Longest Increasing Subsequence*.

**Algorithm**

Let `longest[i, j]` be the longest path ending in `[i, j]`.  Then `longest[j, k] = longest[i, j] + 1` if `(i, j)` and `(j, k)` are connected.  Since `i` is uniquely determined as `A.index(A[k] - A[j])`, this is efficient: we check for each `j < k` what `i` is potentially, and update `longest[j, k]` accordingly.

<iframe src="https://leetcode.com/playground/vEtztLgc/shared" frameBorder="0" width="100%" height="463" name="vEtztLgc"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N \log M)$$, where $$M$$ is the largest element of `A`.  We can show that the number of elements in a subsequence is bounded by $$O(\log \frac{M}{a})$$ where $$a$$ is the minimum element in the subsequence.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
