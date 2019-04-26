# 0961 - N-Repeated Element in Size 2N Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Hash Table | [Leetcode](https://leetcode.com/problems/n-repeated-element-in-size-2n-array) | [solution](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/solution/)


-----------

<p>In a array <code>A</code> of size <code>2N</code>, there are <code>N+1</code> unique elements, and exactly one of these elements is repeated N times.</p>

<p>Return the element repeated <code>N</code> times.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3,3]</span>
<strong>Output: </strong><span id="example-output-1">3</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[2,1,2,5,3,2]</span>
<strong>Output: </strong><span id="example-output-2">2</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[5,1,5,2,5,3,5,4]</span>
<strong>Output: </strong><span id="example-output-3">5</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>4 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt; 10000</code></li>
	<li><code>A.length</code> is even</li>
</ol>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Count

**Intuition and Algorithm**

Let's count the number of elements.  We can use a `HashMap` or an array - here, we use a `HashMap`.

After, the element with a count larger than 1 must be the answer.

<iframe src="https://leetcode.com/playground/Xu4ee6QT/shared" frameBorder="0" width="100%" height="293" name="Xu4ee6QT"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Compare

**Intuition and Algorithm**

If we ever find a repeated element, it must be the answer.  Let's call this answer the *major element*.

Consider all subarrays of length 4.  There must be a major element in at least one such subarray.

This is because either:

* There is a major element in a length 2 subarray, or;
* Every length 2 subarray has exactly 1 major element, which means that a length 4 subarray that begins at a major element will have 2 major elements.

Thus, we only have to compare elements with their neighbors that are distance 1, 2, or 3 away.

<iframe src="https://leetcode.com/playground/9URvAsjC/shared" frameBorder="0" width="100%" height="225" name="9URvAsjC"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
