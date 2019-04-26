# 0859 - Buddy Strings

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | String | [Leetcode](https://leetcode.com/problems/buddy-strings) | [solution](https://leetcode.com/problems/buddy-strings/solution/)


-----------

<p>Given two strings <code>A</code> and <code>B</code>&nbsp;of lowercase letters, return <code>true</code> if and only if we&nbsp;can swap two letters in <code>A</code> so that the result equals <code>B</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<div>
<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">&quot;ab&quot;</span>, B = <span id="example-input-1-2">&quot;ba&quot;</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">&quot;ab&quot;</span>, B = <span id="example-input-2-2">&quot;ab&quot;</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-3-1">&quot;aa&quot;</span>, B = <span id="example-input-3-2">&quot;aa&quot;</span>
<strong>Output: </strong><span id="example-output-3">true</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-4-1">&quot;aaaaaaabc&quot;</span>, B = <span id="example-input-4-2">&quot;aaaaaaacb&quot;</span>
<strong>Output: </strong><span id="example-output-4">true</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-5-1">&quot;&quot;</span>, B = <span id="example-input-5-2">&quot;aa&quot;</span>
<strong>Output: </strong><span id="example-output-5">false</span>
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 20000</code></li>
	<li><code>0 &lt;= B.length &lt;= 20000</code></li>
	<li><code>A</code> and&nbsp;<code>B</code> consist only of lowercase letters.</li>
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
#### Approach 1: Enumerate Cases

**Intuition**

Let's say `i` is *matched* if `A[i] == B[i]`, otherwise `i` is *unmatched*.  A buddy string has almost all matches, because a swap only affects two indices.

If swapping `A[i]` and `A[j]` would demonstrate that `A` and `B` are buddy strings, then `A[i] == B[j]` and `A[j] == B[i]`.  That means among the four free variables `A[i], A[j], B[i], B[j]`, there are only two cases: either `A[i] == A[j]` or not.

**Algorithm**

Let's work through the cases.

In the case `A[i] == A[j] == B[i] == B[j]`, then the strings `A` and `B` are equal.  So if `A == B`, we should check each index `i` for two matches with the same value.

In the case `A[i] == B[j], A[j] == B[i], (A[i] != A[j])`, the rest of the indices match.  So if `A` and `B` have only two unmatched indices (say `i` and `j`), we should check that the equalities `A[i] == B[j]` and `A[j] == B[i]` hold.

<iframe src="https://leetcode.com/playground/3ce2yPsD/shared" frameBorder="0" width="100%" height="500" name="3ce2yPsD"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A` and `B`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
