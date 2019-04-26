# 0862 - Shortest Subarray with Sum at Least K

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Binary Search, Queue | [Leetcode](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k) | [solution](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/solution/)


-----------

<p>Return the <strong>length</strong> of the shortest, non-empty, contiguous&nbsp;subarray of <code>A</code> with sum at least <code>K</code>.</p>

<p>If there is no non-empty subarray with sum at least <code>K</code>, return <code>-1</code>.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1]</span>, K = <span id="example-input-1-2">1</span>
<strong>Output: </strong><span id="example-output-1">1</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[1,2]</span>, K = <span id="example-input-2-2">4</span>
<strong>Output: </strong><span id="example-output-2">-1</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[2,-1,2]</span>, K = <span id="example-input-3-2">3</span>
<strong>Output: </strong><span id="example-output-3">3</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 50000</code></li>
	<li><code>-10 ^ 5&nbsp;&lt;= A[i] &lt;= 10 ^ 5</code></li>
	<li><code>1 &lt;= K &lt;= 10 ^ 9</code></li>
</ol>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Sliding Window

**Intuition**

We can rephrase this as a problem about the prefix sums of `A`.  Let `P[i] = A[0] + A[1] + ... + A[i-1]`.  We want the smallest `y-x` such that `y > x` and `P[y] - P[x] >= K`.

Motivated by that equation, let `opt(y)` be the largest `x` such that `P[x] <= P[y] - K`.  We need two key observations:

* If `x1 < x2` and `P[x2] <= P[x1]`, then `opt(y)` can never be `x1`, as if `P[x1] <= P[y] - K`, then `P[x2] <= P[x1] <= P[y] - K` but `y - x2` is smaller.  This implies that our candidates `x` for `opt(y)` will have increasing values of `P[x]`.

* If `opt(y1) = x`, then we do not need to consider this `x` again.  For if we find some `y2 > y1` with `opt(y2) = x`, then it represents an answer of `y2 - x` which is worse (larger) than `y1 - x`.

**Algorithm**

Maintain a "monoqueue" of indices of `P`: a deque of indices `x_0, x_1, ...` such that `P[x_0], P[x_1], ...` is increasing.

When adding a new index `y`, we'll pop `x_i` from the end of the deque so that `P[x_0], P[x_1], ..., P[y]` will be increasing.

If `P[y] >= P[x_0] + K`, then (as previously described), we don't need to consider this `x_0` again, and we can pop it from the front of the deque.

<iframe src="https://leetcode.com/playground/RnfeP3KD/shared" frameBorder="0" width="100%" height="463" name="RnfeP3KD"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
