# 0976 - Largest Perimeter Triangle

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Math, Sort | [Leetcode](https://leetcode.com/problems/largest-perimeter-triangle) | [solution](https://leetcode.com/problems/largest-perimeter-triangle/solution/)


-----------

<p>Given an array <code>A</code> of positive lengths, return the largest perimeter of a triangle with <strong>non-zero area</strong>, formed from 3 of these lengths.</p>

<p>If it is impossible to form any&nbsp;triangle of non-zero area, return <code>0</code>.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[2,1,2]</span>
<strong>Output: </strong><span id="example-output-1">5</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,2,1]</span>
<strong>Output: </strong><span id="example-output-2">0</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[3,2,3,4]</span>
<strong>Output: </strong><span id="example-output-3">10</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[3,6,2,3]</span>
<strong>Output: </strong><span id="example-output-4">8</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>3 &lt;= A.length &lt;= 10000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 10^6</code></li>
</ol>
</div>
</div>
</div>
</div>

-----------


## Similar Problems

- [Easy] [Largest Triangle Area](largest-triangle-area)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Sort

**Intuition**

Without loss of generality, say the sidelengths of the triangle are $$a \leq b \leq c$$.  The necessary and sufficient condition for these lengths to form a triangle of non-zero area is $$a + b > c$$.

Say we knew $$c$$ already.  There is no reason not to choose the largest possible $$a$$ and $$b$$ from the array.  If $$a + b > c$$, then it forms a triangle, otherwise it doesn't.

**Algorithm**

This leads to a simple algorithm:  Sort the array.  For any $$c$$ in the array, we choose the largest possible $$a \leq b \leq c$$:  these are just the two values adjacent to $$c$$.  If this forms a triangle, we return the answer.

<iframe src="https://leetcode.com/playground/2RjnrKEg/shared" frameBorder="0" width="100%" height="208" name="2RjnrKEg"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
