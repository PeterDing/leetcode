# 0962 - Maximum Width Ramp

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array | [Leetcode](https://leetcode.com/problems/maximum-width-ramp) | [solution](https://leetcode.com/problems/maximum-width-ramp/solution/)


-----------

<p>Given an array <code>A</code> of integers, a <em>ramp</em>&nbsp;is a tuple <code>(i, j)</code> for which <code>i &lt; j</code>&nbsp;and&nbsp;<code>A[i] &lt;= A[j]</code>.&nbsp; The width of such a&nbsp;ramp is <code>j - i</code>.</p>

<p>Find the maximum width of a ramp in <code>A</code>.&nbsp; If one doesn&#39;t exist, return 0.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[6,0,8,2,1,5]</span>
<strong>Output: </strong><span id="example-output-1">4</span>
<strong>Explanation: </strong>
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[9,8,1,0,1,9,4,0,4,1]</span>
<strong>Output: </strong><span id="example-output-2">7</span>
<strong>Explanation: </strong>
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
</pre>
</div>

<div>
<div>
<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= A.length &lt;= 50000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 50000</code></li>
</ol>
</div>
</div>

<div>
<div>&nbsp;</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Sort

**Intuition and Algorithm**

For all elements like `A[i] = v`, let's write the indices `i` in sorted order of their values `v`.  For example with `A[0] = 7, A[1] = 2, A[2] = 5, A[3] = 4`, we can write the order of indices `i=1, i=3, i=2, i=0`.

Then, whenever we write an index `i`, we know there was a ramp of width `i - min(indexes_previously_written)` (if this quantity is positive).  We can keep track of the minimum of all indexes previously written as `m`.

<iframe src="https://leetcode.com/playground/cTgKu5cw/shared" frameBorder="0" width="100%" height="378" name="cTgKu5cw"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$, depending on the implementation of the sorting function.
<br />
<br />


---
#### Approach 2: Binary Search Candidates

**Intuition**

Consider `i` in decreasing order.  We want to find the largest `j` with `A[j] >= A[i]` if it exists.

Thus, the candidates for `j` are decreasing: if there is `j1 < j2` and `A[j1] <= A[j2]` then we strictly prefer `j2`.

**Algorithm**

Let's keep a list of these candidates `j`.  For example, with `A = [0,8,2,7,5]`, the candidates for `i = 0` would be `candidates = [(v=5, i=4), (v=7, i=3), (v=8, i=1)]`.  We keep the list of `candidates` in decreasing order of `i` and increasing order of `v`.

Now we can binary search to find the largest `j` with `A[j] >= A[i]`: it's the first one in this list of candidates with `v >= A[i]`.

<iframe src="https://leetcode.com/playground/jtYswxPE/shared" frameBorder="0" width="100%" height="500" name="jtYswxPE"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
