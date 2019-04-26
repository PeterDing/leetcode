# 0977 - Squares of a Sorted Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array, Two Pointers | [Leetcode](https://leetcode.com/problems/squares-of-a-sorted-array) | [solution](https://leetcode.com/problems/squares-of-a-sorted-array/solution/)


-----------

<p>Given an array of integers <code>A</code>&nbsp;sorted in non-decreasing order,&nbsp;return an array of the squares of each number,&nbsp;also in sorted non-decreasing order.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[-4,-1,0,3,10]</span>
<strong>Output: </strong><span id="example-output-1">[0,1,9,16,100]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[-7,-3,2,3,11]</span>
<strong>Output: </strong><span id="example-output-2">[4,9,9,49,121]</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code><span>1 &lt;= A.length &lt;= 10000</span></code></li>
	<li><code>-10000 &lt;= A[i] &lt;= 10000</code></li>
	<li><code>A</code>&nbsp;is sorted in non-decreasing order.</li>
</ol>
</div>
</div>

-----------


## Similar Problems

- [Easy] [Merge Sorted Array](merge-sorted-array)

- [Medium] [Sort Transformed Array](sort-transformed-array)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Sort

**Intuition and Algorithm**

Create an array of the squares of each element, and sort them.

<iframe src="https://leetcode.com/playground/mVRPMKjB/shared" frameBorder="0" width="100%" height="242" name="mVRPMKjB"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Two Pointer

**Intuition**

Since the array `A` is sorted, loosely speaking it has some negative elements with squares in decreasing order, then some non-negative elements with squares in increasing order.

For example, with `[-3, -2, -1, 4, 5, 6]`, we have the negative part `[-3, -2, -1]` with squares `[9, 4, 1]`, and the positive part `[4, 5, 6]` with squares `[16, 25, 36]`.  Our strategy is to iterate over the negative part in reverse, and the positive part in the forward direction.

**Algorithm**

We can use two pointers to read the positive and negative parts of the array - one pointer `j` in the positive direction, and another `i` in the negative direction.

Now that we are reading two increasing arrays (the squares of the elements), we can merge these arrays together using a two-pointer technique.

<iframe src="https://leetcode.com/playground/h7YnwCLs/shared" frameBorder="0" width="100%" height="500" name="h7YnwCLs"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
