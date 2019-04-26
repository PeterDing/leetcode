# 0922 - Sort Array By Parity II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array, Sort | [Leetcode](https://leetcode.com/problems/sort-array-by-parity-ii) | [solution](https://leetcode.com/problems/sort-array-by-parity-ii/solution/)


-----------

<p>Given an array <code>A</code>&nbsp;of non-negative integers, half of the integers in A are odd, and half of the integers are even.</p>

<p>Sort the array so that whenever <code>A[i]</code> is odd, <code>i</code> is odd; and whenever <code>A[i]</code> is even, <code>i</code> is even.</p>

<p>You may return any answer array that satisfies this condition.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[4,2,5,7]</span>
<strong>Output: </strong><span id="example-output-1">[4,5,2,7]</span>
<strong>Explanation: </strong>[4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= A.length &lt;= 20000</code></li>
	<li><code>A.length % 2 == 0</code></li>
	<li><code>0 &lt;= A[i] &lt;= 1000</code></li>
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
#### Approach 1: Two Pass

**Intuition and Algorithm**

Read all the even integers and put them into places `ans[0]`, `ans[2]`, `ans[4]`, and so on.

Then, read all the odd integers and put them into places `ans[1]`, `ans[3]`, `ans[5]`, etc.

<iframe src="https://leetcode.com/playground/sV3wKPcR/shared" frameBorder="0" width="100%" height="429" name="sV3wKPcR"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Read / Write Heads

**Intuition**

We are motivated (perhaps by the interviewer) to pursue a solution where we modify the original array `A` in place.

First, it is enough to put all even elements in the correct place, since all odd elements will be in the correct place too.  So let's only focus on `A[0], A[2], A[4], ...`

Ideally, we would like to have some partition where everything to the left is already correct, and everything to the right is undecided.

Indeed, this idea works if we separate it into two slices `even = A[0], A[2], A[4], ...` and `odd = A[1], A[3], A[5], ...`.  Our invariant will be that everything less than `i` in the even slice is correct, and everything less than `j` in the odd slice is correct.

**Algorithm**

For each even `i`, let's make `A[i]` even.  To do it, we will draft an element from the odd slice.  We pass `j` through the odd slice until we find an even element, then swap.  Our invariant is maintained, so the algorithm is correct.

<iframe src="https://leetcode.com/playground/aWm3c7PK/shared" frameBorder="0" width="100%" height="344" name="aWm3c7PK"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
