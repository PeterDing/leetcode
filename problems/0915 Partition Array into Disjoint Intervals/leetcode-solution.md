# 0915 - Partition Array into Disjoint Intervals

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array | [Leetcode](https://leetcode.com/problems/partition-array-into-disjoint-intervals) | [solution](https://leetcode.com/problems/partition-array-into-disjoint-intervals/solution/)


-----------

<p>Given an array <code>A</code>, partition it&nbsp;into two (contiguous) subarrays&nbsp;<code>left</code>&nbsp;and <code>right</code>&nbsp;so that:</p>

<ul>
	<li>Every element in <code>left</code>&nbsp;is less than or equal to every element in <code>right</code>.</li>
	<li><code>left</code> and <code>right</code> are non-empty.</li>
	<li><code>left</code>&nbsp;has the smallest possible size.</li>
</ul>

<p>Return the <strong>length</strong> of <code>left</code> after such a partitioning.&nbsp; It is guaranteed that such a partitioning exists.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[5,0,3,8,6]</span>
<strong>Output: </strong><span id="example-output-1">3</span>
<strong>Explanation: </strong>left = [5,0,3], right = [8,6]
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,1,1,0,6,12]</span>
<strong>Output: </strong><span id="example-output-2">4</span>
<strong>Explanation: </strong>left = [1,1,1,0], right = [6,12]
</pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= A.length&nbsp;&lt;= 30000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^6</code></li>
	<li>It is guaranteed there is at least one way to partition <code>A</code> as described.</li>
</ol>

<div>
<div>&nbsp;</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Next Array

**Intuition**

Instead of checking whether `all(L <= R for L in left for R in right)`, let's check whether `max(left) <= min(right)`.

**Algorithm**

Let's try to find `max(left)` for subarrays `left = A[:1], left = A[:2], left =  A[:3], ...` etc.  Specifically, `maxleft[i]` will be the maximum of subarray `A[:i]`.  They are related to each other: `max(A[:4]) = max(max(A[:3]), A[3])`, so `maxleft[4] = max(maxleft[3], A[3])`.

Similarly, `min(right)` for every possible `right` can be found in linear time.

After we have a way to query `max(left)` and `min(right)` quickly, the solution is straightforward.

<iframe src="https://leetcode.com/playground/icvccGCi/shared" frameBorder="0" width="100%" height="480" name="icvccGCi"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
