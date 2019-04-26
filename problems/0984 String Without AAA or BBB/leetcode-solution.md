# 0984 - String Without AAA or BBB

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Greedy | [Leetcode](https://leetcode.com/problems/string-without-aaa-or-bbb) | [solution](https://leetcode.com/problems/string-without-aaa-or-bbb/solution/)


-----------

<p>Given two integers <code>A</code> and <code>B</code>, return <strong>any</strong> string <code>S</code> such that:</p>

<ul>
	<li><code>S</code> has length <code>A + B</code> and contains exactly <code>A</code> <code>&#39;a&#39;</code> letters, and exactly <code>B</code> <code>&#39;b&#39;</code> letters;</li>
	<li>The substring&nbsp;<code>&#39;aaa&#39;</code>&nbsp;does not occur in <code>S</code>;</li>
	<li>The substring <code>&#39;bbb&#39;</code> does not occur in <code>S</code>.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">1</span>, B = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">&quot;abb&quot;
</span><strong>Explanation:</strong> &quot;abb&quot;, &quot;bab&quot; and &quot;bba&quot; are all correct answers.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">4</span>, B = <span id="example-input-2-2">1</span>
<strong>Output: </strong><span id="example-output-2">&quot;aabaa&quot;</span></pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A &lt;= 100</code></li>
	<li><code>0 &lt;= B &lt;= 100</code></li>
	<li>It is guaranteed such an <code>S</code> exists for the given <code>A</code> and <code>B</code>.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Greedy

**Intuition**

Intuitively, we should write the most common letter first.  For example, if we have `A = 6, B = 2`, we want to write `'aabaabaa'`.  The only time we don't write the most common letter is if the last two letters we have written are also the most common letter

**Algorithm**

Let's maintain `A, B`: the number of `'a'` and `'b'`'s left to write.

If we have already written the most common letter twice, we'll write the other letter.  Otherwise, we'll write the most common letter.

<iframe src="https://leetcode.com/playground/Ps9koK2t/shared" frameBorder="0" width="100%" height="500" name="Ps9koK2t"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(A+B)$$.

* Space Complexity:  $$O(A+B)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
