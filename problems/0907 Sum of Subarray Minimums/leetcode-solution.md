# 0907 - Sum of Subarray Minimums

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Stack | [Leetcode](https://leetcode.com/problems/sum-of-subarray-minimums) | [solution](https://leetcode.com/problems/sum-of-subarray-minimums/solution/)


-----------

<p>Given an array of integers <code>A</code>, find the sum of <code>min(B)</code>, where <code>B</code> ranges over&nbsp;every (contiguous) subarray of <code>A</code>.</p>

<p>Since the answer may be large, <strong>return the answer modulo <code>10^9 + 7</code>.</strong></p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,1,2,4]</span>
<strong>Output: </strong><span id="example-output-1">17</span>
<strong>Explanation:</strong> Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.&nbsp; Sum is 17.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 30000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 30000</code></li>
</ol>

<div>
<p>&nbsp;</p>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Prev/Next Array

**Intuition**

Let's try to count the number of subarrays `#(j)` for which `A[j]` is the *right-most* minimum.  Then, the answer will be `sum #(j) * A[j]`.  (We must say *right-most* so that we form disjoint sets of subarrays and do not double count any, as the minimum of an array may not be unique.)

This in turn brings us the question of knowing the smallest index `i <= j` for which `A[i], A[i+1], ..., A[j]` are all `>= A[j]`; and the largest index `k >= j` for which `A[j+1], A[j+2], ..., A[k]` are all `> A[j]`.

**Algorithm**

For example, if `A = [10, 3, 4, 5, _3_, 2, 3, 10]` and we would like to know `#(j = 4)` [the count of the second `3`, which is marked], we would find `i = 1` and `k = 5`.

From there, the actual count is `#(j) = (j - i + 1) * (k - j + 1)`, as there are `j - i + 1` choices `i, i+1, ..., j` for the left index of the subarray, and `k - j + 1` choices `j, j+1, ..., k` for the right index of the subarray.

Answering these queries (ie. determining `(i, k)` given `j`) is a classic problem that can be answered with a stack.  We'll focus on the problem of finding `i`: the problem of finding `k` is similar.

**Making a Prev Array**

The idea is to maintain `stack`, a monotone decreasing subsequence of `A` (actually, indices of `A` in implementation).  These represent candidate boundaries `i* - 1` for the next query, stored in increasing order of `A[i*]`.

Now considering `j` in increasing order, we can remove candidates for which `A[i*] <= A[j]` in decreasing order of `i*`.

For example, if `A = [10, 5, 3, 7, 0, 4, 5, 2, 1, _8_]`, then when considering `j = 9` `(A[j] = 8)`, we have a stack of boundaries like `[-1, 0, 3, 6]` (representing `A[i*] = -inf, 10, 7, 5`).  We pop `6` and `3` from the stack, as `5 <= 8` and `7 <= 8`, and we get the answer boundary `i* - 1 = 0`.

Note that this process is linear, since we do a linear amount of pushes and pops of the stack in total.

This is quite difficult to figure out, but this type of technique occurs often in many other problems, so it is worth learning in detail.

<iframe src="https://leetcode.com/playground/CMceXvyZ/shared" frameBorder="0" width="100%" height="500" name="CMceXvyZ"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Maintain Stack of Minimums

**Intuition**

For a specific `j`, let's try to count the minimum of each subarray `[i, j]`.  The intuition is that as we increment `j++`, these minimums may be related to each other.  Indeed, `min(A[i:j+1]) = min(A[i:j], A[j])`.

Playing with some array like `A = [1,7,5,2,4,3,9]`, with `j = 6` the minimum of each subarray `[i, j]` is `B = [1,2,2,2,3,3,9]`.   We can see that there are critical points `i = 0, i = 3, i = 5, i = 6` where a minimum is reached for the first time when walking left from `j`.

**Algorithm**

Let's try to maintain an RLE (run length encoding) of these critical points `B`.  More specifically, for the above `(A, j)`, we will maintain `stack = [(val=1, count=1), (val=2, count=3), (val=3, count=2), (val=9, count=1)]`, that represents a run length encoding of the subarray minimums `B = [1,2,2,2,3,3,9]`.  For each `j`, we want `sum(B)`.  

As we increment `j`, we will have to update this stack to include the newest element `(val=x, count=1)`.  We need to pop off all values `>= x` before, as the minimum of the associated subarray `[i, j]` will now be `A[j]` instead of what it was before.

At the end, the answer is the dot product of this stack: $$\sum\limits_{e\text{ } \in \text{ stack}} e\text{.val} * e\text{.count}$$, which we also maintain on the side as the variable `dot`.

<iframe src="https://leetcode.com/playground/yoG86DGx/shared" frameBorder="0" width="100%" height="500" name="yoG86DGx"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).  Approach 2 inspired by [@aakarshmadhavan](https://leetcode.com/aakarshmadhavan).
