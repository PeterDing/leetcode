# 0896 - Monotonic Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/monotonic-array) | [solution](https://leetcode.com/problems/monotonic-array/solution/)


-----------

<p>An array is <em>monotonic</em> if it is either monotone increasing or monotone decreasing.</p>

<p>An array <code>A</code> is monotone increasing if for all <code>i &lt;= j</code>, <code>A[i] &lt;= A[j]</code>.&nbsp; An array <code>A</code> is monotone decreasing if for all <code>i &lt;= j</code>, <code>A[i] &gt;= A[j]</code>.</p>

<p>Return <code>true</code> if and only if the given array <code>A</code> is monotonic.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,2,3]</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[6,5,4,4]</span>
<strong>Output: </strong><span id="example-output-2">true</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,3,2]</span>
<strong>Output: </strong><span id="example-output-3">false</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[1,2,4,5]</span>
<strong>Output: </strong><span id="example-output-4">true</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-5-1">[1,1,1]</span>
<strong>Output: </strong><span id="example-output-5">true</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 50000</code></li>
	<li><code>-100000 &lt;= A[i] &lt;= 100000</code></li>
</ol>
</div>
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
#### Approach 1: Two Pass

**Intuition**

An array is *monotonic* if it is monotone increasing, or monotone decreasing.  Since `a <= b` and `b <= c` implies `a <= c`, we only need to check adjacent elements to determine if the array is monotone increasing (or decreasing, respectively).  We can check each of these properties in one pass.

**Algorithm**

To check whether an array `A` is monotone increasing, we'll check `A[i] <= A[i+1]` for all `i`.  The check for monotone decreasing is similar.

<iframe src="https://leetcode.com/playground/45YrvCAw/shared" frameBorder="0" width="100%" height="344" name="45YrvCAw"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---
#### Approach 2: One Pass

**Intuition**

To perform this check in one pass, we want to handle a stream of comparisons from $$\{-1, 0, 1\}$$, corresponding to `<`, `==`, or `>`.  For example, with the array `[1, 2, 2, 3, 0]`, we will see the stream `(-1, 0, -1, 1)`.

**Algorithm**

Keep track of `store`, equal to the first non-zero comparison seen (if it exists.)  If we see the opposite comparison, the answer is `False`.

Otherwise, every comparison was (necessarily) in the set $$\{-1, 0\}$$, or every comparison was in the set $$\{0, 1\}$$, and therefore the array is monotonic.

<iframe src="https://leetcode.com/playground/qcBYT2JK/shared" frameBorder="0" width="100%" height="310" name="qcBYT2JK"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---
#### Approach 3: One Pass (Simple Variant)

**Intuition and Algorithm**

To perform this check in one pass, we want to remember if it is monotone increasing or monotone decreasing.

It's monotone increasing if there aren't some adjacent values `A[i], A[i+1]` with `A[i] > A[i+1]`, and similarly for monotone decreasing.

If it is either monotone increasing or monotone decreasing, then `A` is monotonic.

<iframe src="https://leetcode.com/playground/FnWYKTw8/shared" frameBorder="0" width="100%" height="293" name="FnWYKTw8"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
