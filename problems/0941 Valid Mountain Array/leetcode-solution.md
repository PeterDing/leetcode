# 0941 - Valid Mountain Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/valid-mountain-array) | [solution](https://leetcode.com/problems/valid-mountain-array/solution/)


-----------

<p>Given an array <code>A</code> of integers, return <code>true</code> if and only if it is a <em>valid mountain array</em>.</p>

<p>Recall that A is a mountain array if and only if:</p>

<ul>
	<li><code>A.length &gt;= 3</code></li>
	<li>There exists some <code>i</code> with&nbsp;<code>0 &lt; i&nbsp;&lt; A.length - 1</code>&nbsp;such that:
	<ul>
		<li><code>A[0] &lt; A[1] &lt; ... A[i-1] &lt; A[i] </code></li>
		<li><code>A[i] &gt; A[i+1] &gt; ... &gt; A[B.length - 1]</code></li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[2,1]</span>
<strong>Output: </strong><span id="example-output-1">false</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[3,5,5]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[0,3,2,1]</span>
<strong>Output: </strong><span id="example-output-3">true</span></pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10000&nbsp;</code></li>
</ol>

<div>
<p>&nbsp;</p>

<div>
<div>&nbsp;</div>
</div>
</div>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: One Pass

**Intuition**

If we walk along the mountain from left to right, we have to move strictly up, then strictly down.

**Algorithm**

Let's walk up from left to right until we can't: that has to be the peak.  We should ensure the peak is not the first or last element.  Then, we walk down.  If we reach the end, the array is valid, otherwise its not.

<iframe src="https://leetcode.com/playground/yszb4GTC/shared" frameBorder="0" width="100%" height="395" name="yszb4GTC"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
