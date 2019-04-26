# 0821 - Shortest Distance to a Character

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy |  | [Leetcode](https://leetcode.com/problems/shortest-distance-to-a-character) | [solution](https://leetcode.com/problems/shortest-distance-to-a-character/solution/)


-----------

<p>Given a string <code>S</code>&nbsp;and a character <code>C</code>, return an array of integers representing the shortest distance from the character <code>C</code> in the string.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> S = &quot;loveleetcode&quot;, C = &#39;e&#39;
<strong>Output:</strong> [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>S</code> string length is&nbsp;in&nbsp;<code>[1, 10000].</code></li>
	<li><code>C</code>&nbsp;is a single character, and guaranteed to be in string <code>S</code>.</li>
	<li>All letters in <code>S</code> and <code>C</code> are lowercase.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Min Array [Accepted]

**Intuition**

For each index `S[i]`, let's try to find the distance to the next character `C` going left, and going right.  The answer is the minimum of these two values.

**Algorithm**

When going left to right, we'll remember the index `prev` of the last character `C` we've seen.  Then the answer is `i - prev`.

When going right to left, we'll remember the index `prev` of the last character `C` we've seen.  Then the answer is `prev - i`.

We take the minimum of these two answers to create our final answer.

<iframe src="https://leetcode.com/playground/oPmtNjJL/shared" frameBorder="0" width="100%" height="395" name="oPmtNjJL"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.  We scan through the string twice.

* Space Complexity: $$O(N)$$, the size of `ans`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
