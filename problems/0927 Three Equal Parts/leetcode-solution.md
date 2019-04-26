# 0927 - Three Equal Parts

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Math, Binary Search, Greedy | [Leetcode](https://leetcode.com/problems/three-equal-parts) | [solution](https://leetcode.com/problems/three-equal-parts/solution/)


-----------

<p>Given an array <code>A</code> of <code>0</code>s and <code>1</code>s, divide the array into 3 non-empty parts such that all of these parts represent the same binary value.</p>

<p>If it is possible, return <strong>any</strong> <code>[i, j]</code>&nbsp;with <code>i+1 &lt; j</code>, such that:</p>

<ul>
	<li><code>A[0], A[1], ..., A[i]</code> is the first part;</li>
	<li><code>A[i+1], A[i+2], ..., A[j-1]</code> is the second part, and</li>
	<li><code>A[j], A[j+1], ..., A[A.length - 1]</code> is the third part.</li>
	<li>All three parts have equal binary value.</li>
</ul>

<p>If it is not possible, return <code>[-1, -1]</code>.</p>

<p>Note that the entire part is used when considering what binary value it represents.&nbsp; For example, <code>[1,1,0]</code>&nbsp;represents <code>6</code>&nbsp;in decimal,&nbsp;not <code>3</code>.&nbsp; Also, leading zeros are allowed, so&nbsp;<code>[0,1,1]</code> and <code>[1,1]</code> represent the same value.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,0,1,0,1]</span>
<strong>Output: </strong><span id="example-output-1">[0,3]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,1,0,1,1]</span>
<strong>Output: </strong><span id="example-output-2">[-1,-1]</span></pre>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>3 &lt;= A.length &lt;= 30000</code></li>
	<li><code>A[i] == 0</code>&nbsp;or <code>A[i] == 1</code></li>
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
#### Approach 1: Equal Ones

**Intuition**

Each part has to have the same number of ones in their representation.  The algorithm given below is the natural continuation of this idea.

**Algorithm**

Say `S` is the number of ones in `A`.  Since every part has the same number of ones, they all should have `T = S / 3` ones.

If `S` isn't divisible by 3, the task is impossible.

We can find the position of the 1st, T-th, T+1-th, 2T-th, 2T+1-th, and 3T-th one.  The positions of these ones form 3 intervals: `[i1, j1], [i2, j2], [i3, j3]`.  (If there are only 3 ones, then the intervals are each length 1.)

Between them, there may be some number of zeros.  The zeros after `j3` must be included in each part: say there are `z` of them `(z = S.length - j3)`.

So the first part, `[i1, j1]`, is now `[i1, j1+z]`.  Similarly, the second part, `[i2, j2]`, is now `[i2, j2+z]`.

If all this is actually possible, then the final answer is `[j1+z, j2+z+1]`.

<iframe src="https://leetcode.com/playground/svqa2QF7/shared" frameBorder="0" width="100%" height="500" name="svqa2QF7"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
