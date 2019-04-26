# 0908 - Smallest Range I

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Math | [Leetcode](https://leetcode.com/problems/smallest-range-i) | [solution](https://leetcode.com/problems/smallest-range-i/solution/)


-----------

<p>Given an array <code>A</code> of integers, for each integer <code>A[i]</code> we may choose any <code>x</code> with <code>-K &lt;= x &lt;= K</code>, and add <code>x</code> to <code>A[i]</code>.</p>

<p>After this process, we have some array <code>B</code>.</p>

<p>Return the smallest possible difference between the maximum value of <code>B</code>&nbsp;and the minimum value of <code>B</code>.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1]</span>, K = <span id="example-input-1-2">0</span>
<strong>Output: </strong><span id="example-output-1">0
<strong>Explanation</strong>: B = [1]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[0,10]</span>, K = <span id="example-input-2-2">2</span>
<strong>Output: </strong><span id="example-output-2">6
</span><span id="example-output-1"><strong>Explanation</strong>: B = [2,8]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[1,3,6]</span>, K = <span id="example-input-3-2">3</span>
<strong>Output: </strong><span id="example-output-3">0
</span><span id="example-output-1"><strong>Explanation</strong>: B = [3,3,3] or B = [4,4,4]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10000</code></li>
	<li><code>0 &lt;= K &lt;= 10000</code></li>
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
#### Approach 1: Mathematical

**Intuition and Algorithm**

Let `A` be the original array, and `B` be the array after all our modifications.  Towards trying to minimize `max(B) - min(B)`, let's try to minimize `max(B)` and maximize `min(B)` separately.

The smallest possible value of `max(B)` is `max(A) - K`, as the value `max(A)` cannot go lower.  Similarly, the largest possible value of `min(B)` is `min(A) + K`.  So the quantity `max(B) - min(B)` is at least `ans = (max(A) - K) - (min(A) + K)`.

We can attain this value (if `ans >= 0`), by the following modifications:

* If $$A[i] \leq \min(A) + K$$, then $$B[i] = \min(A) + K$$
* Else, if $$A[i] \geq \max(A) - K$$, then $$B[i] = \max(A) - K$$
* Else, $$B[i] = A[i]$$.

If `ans < 0`, the best answer we could have is `ans = 0`, also using the same modification.

<iframe src="https://leetcode.com/playground/hn3nSh7u/shared" frameBorder="0" width="100%" height="225" name="hn3nSh7u"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---

Analysis written by: [@awice](https://leetcode.com/awice).
