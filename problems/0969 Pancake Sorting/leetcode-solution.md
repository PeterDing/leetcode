# 0969 - Pancake Sorting

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Sort | [Leetcode](https://leetcode.com/problems/pancake-sorting) | [solution](https://leetcode.com/problems/pancake-sorting/solution/)


-----------

<p>Given an array <code>A</code>, we can perform a&nbsp;<em>pancake flip</em>:&nbsp;We choose some positive integer&nbsp;<code><strong>k</strong> &lt;= A.length</code>, then reverse the order of the first <strong>k</strong> elements of <code>A</code>.&nbsp; We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array <code>A</code>.</p>

<p>Return the k-values corresponding to a sequence of pancake flips that sort <code>A</code>.&nbsp; Any&nbsp;valid answer that sorts the array within <code>10 * A.length</code> flips will be judged as correct.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,2,4,1]</span>
<strong>Output: </strong><span id="example-output-1">[4,2,4,3]</span>
<strong>Explanation: </strong>
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted. 
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,2,3]</span>
<strong>Output: </strong><span id="example-output-2">[]</span>
<strong>Explanation: </strong>The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.
</pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 100</code></li>
	<li><code>A[i]</code> is a permutation of <code>[1, 2, ..., A.length]</code></li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Sort Largest to Smallest

**Intuition**

We can place the largest element (in location `i`, 1-indexed) by flipping `i` to move the element to the first position, then `A.length` to move it to the last position.  Afterwards, the largest element is in the correct position, so we no longer need to pancake-flip by `A.length` or more.

We can repeat this process until the array is sorted.  Each move will use 2 flips per element.

**Algorithm**

First, sort the locations from largest value of A to smallest value of A.

For each element (from largest to smallest) with location `i`, we will first simulate where this element actually is, based on the pancake flips we have done.  For a pancake flip `f`, if `i <= f`, then the element has moved from location `i` to `f+1 - i`.

After, we flip by `i` then `N--` to put this element in the correct position.

<iframe src="https://leetcode.com/playground/kQvhoWDb/shared" frameBorder="0" width="100%" height="412" name="kQvhoWDb"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
