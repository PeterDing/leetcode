# 0978 - Longest Turbulent Subarray

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Dynamic Programming, Sliding Window | [Leetcode](https://leetcode.com/problems/longest-turbulent-subarray) | [solution](https://leetcode.com/problems/longest-turbulent-subarray/solution/)


-----------

<p>A subarray <code>A[i], A[i+1], ..., A[j]</code>&nbsp;of <code>A</code> is said to be <em>turbulent</em> if and only if:</p>

<ul>
	<li>For <code>i &lt;= k &lt; j</code>, <code>A[k] &gt; A[k+1]</code> when <code>k</code> is odd, and <code>A[k] &lt; A[k+1]</code> when <code>k</code> is even;</li>
	<li><strong>OR</strong>, for <code>i &lt;= k &lt; j</code>, <code>A[k] &gt; A[k+1]</code> when <code>k</code> is even, and <code>A[k] &lt; A[k+1]</code> when <code>k</code> is odd.</li>
</ul>

<p>That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.</p>

<p>Return the <strong>length</strong> of a&nbsp;maximum size turbulent subarray of A.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[9,4,2,10,7,8,8,1,9]</span>
<strong>Output: </strong><span id="example-output-1">5</span>
<strong>Explanation: </strong>(A[1] &gt; A[2] &lt; A[3] &gt; A[4] &lt; A[5])
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[4,8,12,16]</span>
<strong>Output: </strong><span id="example-output-2">2</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[100]</span>
<strong>Output: </strong><span id="example-output-3">1</span>
</pre>
</div>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 40000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
</ol>

-----------


## Similar Problems

- [Easy] [Maximum Subarray](maximum-subarray)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Sliding Window

**Intuition**

Evidently, we only care about the comparisons between adjacent elements.  If the comparisons are represented by `-1, 0, 1` (for `<, =, >`), then we want the longest sequence of alternating `1, -1, 1, -1, ...` (starting with either `1` or `-1`).

These alternating comparisons form contiguous blocks.  We know when the next block ends: when it is the last two elements being compared, or when the sequence isn't alternating.

For example, take an array like `A = [9,4,2,10,7,8,8,1,9]`.  The comparisons are `[1,1,-1,1,-1,0,-1,1]`.  The blocks are `[1], [1,-1,1,-1], [0], [-1,1]`.

**Algorithm**

Scan the array from left to right.  If we are at the end of a block (last elements OR it stopped alternating), then we should record the length of that block as our candidate answer, and set the start of the new block as the next element.

<iframe src="https://leetcode.com/playground/9pQoKhee/shared" frameBorder="0" width="100%" height="378" name="9pQoKhee"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
