# 0954 - Array of Doubled Pairs

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Hash Table | [Leetcode](https://leetcode.com/problems/array-of-doubled-pairs) | [solution](https://leetcode.com/problems/array-of-doubled-pairs/solution/)


-----------

<p>Given an array of integers <code>A</code>&nbsp;with even length, return <code>true</code> if and only if it is possible to reorder it such that <code>A[2 * i + 1] = 2 * A[2 * i]</code> for every <code>0 &lt;=&nbsp;i &lt; len(A) / 2</code>.</p>

<p>&nbsp;</p>

<div>
<div>
<div>
<ol>
</ol>
</div>
</div>
</div>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[3,1,3,6]</span>
<strong>Output: </strong><span id="example-output-1">false</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[2,1,2,6]</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[4,-2,2,-4]</span>
<strong>Output: </strong><span id="example-output-3">true</span>
<strong>Explanation: </strong><span id="example-output-3">We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[1,2,4,16,8,4]</span>
<strong>Output: </strong><span id="example-output-4">false</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 30000</code></li>
	<li><code>A.length</code> is even</li>
	<li><code>-100000 &lt;= A[i] &lt;= 100000</code></li>
</ol>
</div>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Greedy

**Intuition**

If `x` is currently the array element with the least absolute value, it must pair with `2*x`, as there does not exist any other `x/2` to pair with it.

**Algorithm**

Let's try to (virtually) "write" the final reordered array.

Let's check elements in order of absolute value.  When we check an element `x` and it isn't used, it must pair with `2*x`.  We will attempt to write `x, 2x` - if we can't, then the answer is `false`.  If we write everything, the answer is `true`.

To keep track of what we have not yet written, we will store it in a `count`.

<iframe src="https://leetcode.com/playground/2njGcRUM/shared" frameBorder="0" width="100%" height="500" name="2njGcRUM"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
