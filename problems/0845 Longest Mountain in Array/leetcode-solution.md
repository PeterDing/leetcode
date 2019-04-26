# 0845 - Longest Mountain in Array

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Two Pointers | [Leetcode](https://leetcode.com/problems/longest-mountain-in-array) | [solution](https://leetcode.com/problems/longest-mountain-in-array/solution/)


-----------

<p>Let&#39;s call any (contiguous) subarray B (of A)&nbsp;a <em>mountain</em> if the following properties hold:</p>

<ul>
	<li><code>B.length &gt;= 3</code></li>
	<li>There exists some <code>0 &lt; i&nbsp;&lt; B.length - 1</code> such that <code>B[0] &lt; B[1] &lt; ... B[i-1] &lt; B[i] &gt; B[i+1] &gt; ... &gt; B[B.length - 1]</code></li>
</ul>

<p>(Note that B could be any subarray of A, including the entire array A.)</p>

<p>Given an array <code>A</code>&nbsp;of integers,&nbsp;return the length of the longest&nbsp;<em>mountain</em>.&nbsp;</p>

<p>Return <code>0</code> if there is no mountain.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[2,1,4,7,3,2,5]
<strong>Output: </strong>5
<strong>Explanation: </strong>The largest mountain is [1,4,7,3,2] which has length 5.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>[2,2,2]
<strong>Output: </strong>0
<strong>Explanation: </strong>There is no mountain.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 10000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10000</code></li>
</ol>

<p><strong>Follow up:</strong></p>

<ul>
	<li>Can you solve it using only one pass?</li>
	<li>Can you solve it in <code>O(1)</code> space?</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Two Pointer [Accepted]

**Intuition**

Without loss of generality, a mountain can only start after the previous one ends.

This is because if it starts before the peak, it will be smaller than a mountain starting previous; and it is impossible to start after the peak.

**Algorithm**

For a starting index `base`, let's calculate the length of the longest mountain `A[base], A[base+1], ..., A[end]`.

If such a mountain existed, the next possible mountain will start at `base = end`; if it didn't, then either we reached the end, or we have `A[base] > A[base+1]` and we can start at `base + 1`.

**Example**

Here is a worked example on the array `A = [1, 2, 3, 2, 1, 0, 2, 3, 1]`:

<center>
    <img src="../Figures/845/diagram1.png" alt="Worked example of A = [1,2,3,2,1,0,2,3,1]" style="height: 150px"/>
</center>

<br>

`base` starts at `0`, and `end` travels using the first while loop to `end = 2` (`A[end] = 3`), the potential peak of this mountain.  After, it travels to `end = 5` (`A[end] = 0`) during the second while loop, and a candidate answer of 6 `(base = 0, end = 5)` is recorded.

Afterwards, base is set to `5` and the process starts over again, with `end = 7` the peak of the mountain, and `end = 8` the right boundary, and the candidate answer of 4 `(base = 5, end = 8)` being recorded.

<iframe src="https://leetcode.com/playground/7cVQKFLP/shared" frameBorder="0" width="100%" height="500" name="7cVQKFLP"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
