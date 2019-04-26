# 0852 - Peak Index in a Mountain Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Binary Search | [Leetcode](https://leetcode.com/problems/peak-index-in-a-mountain-array) | [solution](https://leetcode.com/problems/peak-index-in-a-mountain-array/solution/)


-----------

<p>Let&#39;s call an array <code>A</code> a <em>mountain</em>&nbsp;if the following properties hold:</p>

<ul>
	<li><code>A.length &gt;= 3</code></li>
	<li>There exists some <code>0 &lt; i&nbsp;&lt; A.length - 1</code> such that <code>A[0] &lt; A[1] &lt; ... A[i-1] &lt; A[i] &gt; A[i+1] &gt; ... &gt; A[A.length - 1]</code></li>
</ul>

<p>Given an array that is definitely a mountain, return any&nbsp;<code>i</code>&nbsp;such that&nbsp;<code>A[0] &lt; A[1] &lt; ... A[i-1] &lt; A[i] &gt; A[i+1] &gt; ... &gt; A[A.length - 1]</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[0,1,0]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[0,2,1,0]</span>
<strong>Output: </strong><span id="example-output-2">1</span></pre>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>3 &lt;= A.length &lt;= 10000</code></li>
	<li><code><font face="monospace">0 &lt;= A[i] &lt;= 10^6</font></code></li>
	<li>A&nbsp;is a mountain, as defined above.</li>
</ol>


-----------


## Similar Problems

- [Medium] [Find Peak Element](find-peak-element)




## Solution:

[TOC]

---
#### Approach 1: Linear Scan

**Intuition and Algorithm**

The mountain increases until it doesn't.  The point at which it stops increasing is the peak.

<iframe src="https://leetcode.com/playground/wnFAmS4Z/shared" frameBorder="0" width="100%" height="174" name="wnFAmS4Z"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.


---
#### Approach 2: Binary Search

**Intuition and Algorithm**

The comparison `A[i] < A[i+1]` in a mountain array looks like `[True, True, True, ..., True, False, False, ..., False]`: 1 or more boolean `True`s, followed by 1 or more boolean `False`.  For example, in the mountain array `[1, 2, 3, 4, 1]`, the comparisons `A[i] < A[i+1]` would be `True, True, True, False`.

We can binary search over this array of comparisons, to find the largest index `i` such that `A[i] < A[i+1]`.  For more on *binary search*, see the [LeetCode explore topic here.](https://leetcode.com/explore/learn/card/binary-search/)

<iframe src="https://leetcode.com/playground/FoZ3SCRk/shared" frameBorder="0" width="100%" height="276" name="FoZ3SCRk"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\log N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.


---

Analysis written by: [@awice](https://leetcode.com/awice).
