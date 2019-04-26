# 0910 - Smallest Range II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Math, Greedy | [Leetcode](https://leetcode.com/problems/smallest-range-ii) | [solution](https://leetcode.com/problems/smallest-range-ii/solution/)


-----------

<p>Given an array <code>A</code> of integers, for each integer <code>A[i]</code> we need to choose <strong>either&nbsp;<code>x = -K</code>&nbsp;or <code>x = K</code></strong>, and add <code>x</code> to <code>A[i] <strong>(only once)</strong></code>.</p>

<p>After this process, we have some array <code>B</code>.</p>

<p>Return the smallest possible difference between the maximum value of <code>B</code>&nbsp;and the minimum value of <code>B</code>.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1]</span>, K = <span id="example-input-1-2">0</span>
<strong>Output: </strong><span id="example-output-1">0</span>
<span><strong>Explanation</strong>: B = [1]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">[0,10]</span>, K = <span id="example-input-2-2">2</span>
<strong>Output: </strong><span id="example-output-2">6
</span><span><strong>Explanation</strong>: B = [2,8]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">[1,3,6]</span>, K = <span id="example-input-3-2">3</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<span><strong>Explanation</strong>: B = [4,6,3]</span>
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
#### Approach 1: Linear Scan

**Intuition**

As in *Smallest Range I*, smaller `A[i]` will choose to increase their value ("go up"), and bigger `A[i]` will decrease their value ("go down").

**Algorithm**

We can formalize the above concept: if `A[i] < A[j]`, we don't need to consider when `A[i]` goes down while `A[j]` goes up.  This is because the interval `(A[i] + K, A[j] - K)` is a subset of `(A[i] - K, A[j] + K)` (here, `(a, b)` for `a > b` denotes `(b, a)` instead.)

That means that it is never worse to choose `(up, down)` instead of `(down, up)`.  We can prove this claim that one interval is a subset of another, by showing both `A[i] + K` and `A[j] - K` are between `A[i] - K` and `A[j] + K`.

For sorted `A`, say `A[i]` is the largest `i` that goes up.  Then `A[0] + K, A[i] + K, A[i+1] - K, A[A.length - 1] - K` are the only relevant values for calculating the answer: every other value is between one of these extremal values.

<iframe src="https://leetcode.com/playground/cCvupdgy/shared" frameBorder="0" width="100%" height="310" name="cCvupdgy"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of the `A`.

* Space Complexity:  $$O(1)$$, plus the space used by the builtin sorting algorithm.
<br />
<br />


---

Analysis written by: [@awice](https://leetcode.com/awice).
