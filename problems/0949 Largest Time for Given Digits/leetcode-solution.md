# 0949 - Largest Time for Given Digits

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Math | [Leetcode](https://leetcode.com/problems/largest-time-for-given-digits) | [solution](https://leetcode.com/problems/largest-time-for-given-digits/solution/)


-----------

<p>Given an array of 4 digits, return the largest 24 hour time that can be made.</p>

<p>The smallest 24 hour time is 00:00, and the largest is 23:59.&nbsp; Starting from 00:00, a time is larger if more time has elapsed since midnight.</p>

<p>Return the answer as a string of length 5.&nbsp; If no valid time can be made, return an empty string.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[1,2,3,4]</span>
<strong>Output: </strong><span id="example-output-1">&quot;23:41&quot;</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[5,5,5,5]</span>
<strong>Output: </strong><span id="example-output-2">&quot;&quot;</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>A.length == 4</code></li>
	<li><code>0 &lt;= A[i] &lt;= 9</code></li>
</ol>
</div>
</div>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Brute Force

**Intuition**

Try all possible times, and remember the largest one.

**Algorithm (Java)**

Iterate over all permutations `(i, j, k, l)` of `(0, 1, 2, 3)`.  For each permutation, we can try the time `A[i]A[j] : A[k]A[l]`.

This is a valid time if and only if the number of hours `10*A[i] + A[j]` is less than `24`; and the number of minutes `10*A[k] + A[l]` is less than `60`.

We will output the largest valid time.

**Algorithm (Python)**

For each possible ordering of the 4 digits, if it's a legal time and the time is greater than the one we have stored, update the answer.

<iframe src="https://leetcode.com/playground/vzuf8WrS/shared" frameBorder="0" width="100%" height="429" name="vzuf8WrS"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(1)$$.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).  Java implementation inspired by [@rock](https://leetcode.com/problems/largest-time-for-given-digits/discuss/200693/Java-11-liner-O(64)-w-comment-6-ms.).
