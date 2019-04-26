# 0932 - Beautiful Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Divide and Conquer | [Leetcode](https://leetcode.com/problems/beautiful-array) | [solution](https://leetcode.com/problems/beautiful-array/solution/)


-----------

<p>For some fixed <code>N</code>, an array <code>A</code> is <em>beautiful</em> if it is a permutation of the integers <code>1, 2, ..., N</code>, such that:</p>

<p>For every <code>i &lt; j</code>, there is <strong>no</strong>&nbsp;<code>k</code> with <code>i &lt; k &lt; j</code>&nbsp;such that <code>A[k] * 2 = A[i] + A[j]</code>.</p>

<p>Given <code>N</code>, return <strong>any</strong> beautiful array <code>A</code>.&nbsp; (It is guaranteed that one exists.)</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">4</span>
<strong>Output: </strong><span id="example-output-1">[2,1,4,3]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">5</span>
<strong>Output: </strong><span>[3,1,2,5,4]</span></pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= N &lt;= 1000</code></li>
</ul>

<div>
<div>&nbsp;</div>
</div>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---

#### Approach 1: Divide and Conquer

**Intuition**

This answer is quite unintuitive.

First, notice that the condition is equivalent to saying that `A` has no arithmetic subsequence.  We'll use the term "*arithmetic-free*" interchangeably with "*beautiful*".

One way is to guess that we should divide and conquer.  One reason for this is that the condition is linear, so if the condition is satisfied by variables taking on values `(1, 2, ..., n)`, it is satisfied by those variables taking on values `(a + b, a + 2*b, a + 3*b, ..., a + (n-1)*b)` instead.

If we perform a divide and conquer, then we have two parts `left` and `right`, such that each part is arithmetic-free, and we only want that a triple from both parts is not arithmetic.  Looking at the conditions:

* `2*A[k] = A[i] + A[j]`
* `(i < k < j)`, `i` from `left`, `j` from `right`

we can guess that because the left hand side `2*A[k]` is even, we can choose `left` to have all odd elements, and `right` to have all even elements.

Another way we could arrive at this is to try to place a number in the middle, like `5`.  We will have `4` and `6` say, to the left of `5`, and `7` to the right of `6`, etc.  We see that in general, odd numbers move towards one direction and even numbers towards another direction.

One final way we could arrive at this is to inspect possible answers arrived at by brute force.  On experimentation, we see that many answers have all the odd elements to one side, and all the even elements to the other side, with only minor variation.

**Algorithm**

Looking at the elements `1, 2, ..., N`, there are `(N+1) / 2` odd numbers and `N / 2` even numbers.

We solve for elements `1, 2, ..., (N+1) / 2` and map these numbers onto `1, 3, 5, ...`.  Similarly, we solve for elements `1, 2, ..., N/2` and map these numbers onto `2, 4, 6, ...`.

We can compose these solutions by concatenating them, since an arithmetic sequence never starts and ends with elements of different parity.

We memoize the result to arrive at the answer quicker.

<iframe src="https://leetcode.com/playground/3NT7Bgm6/shared" frameBorder="0" width="100%" height="480" name="3NT7Bgm6"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$.  The function `f` is called only $$O(\log N)$$ times, and each time does $$O(N)$$ work.

* Space Complexity:  $$O(N \log N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
