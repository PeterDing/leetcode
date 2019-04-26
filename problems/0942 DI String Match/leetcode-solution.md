# 0942 - DI String Match

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Math | [Leetcode](https://leetcode.com/problems/di-string-match) | [solution](https://leetcode.com/problems/di-string-match/solution/)


-----------

<p>Given a string <code>S</code> that <strong>only</strong> contains &quot;I&quot; (increase) or &quot;D&quot; (decrease), let <code>N = S.length</code>.</p>

<p>Return <strong>any</strong> permutation <code>A</code> of <code>[0, 1, ..., N]</code> such that for all <code>i = 0,&nbsp;..., N-1</code>:</p>

<ul>
	<li>If <code>S[i] == &quot;I&quot;</code>, then <code>A[i] &lt; A[i+1]</code></li>
	<li>If <code>S[i] == &quot;D&quot;</code>, then <code>A[i] &gt; A[i+1]</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;IDID&quot;</span>
<strong>Output: </strong><span id="example-output-1">[0,4,1,3,2]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;III&quot;</span>
<strong>Output: </strong><span id="example-output-2">[0,1,2,3]</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">&quot;DDI&quot;</span>
<strong>Output: </strong><span id="example-output-3">[3,2,0,1]</span></pre>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= S.length &lt;= 10000</code></li>
	<li><code>S</code> only contains characters <code>&quot;I&quot;</code> or <code>&quot;D&quot;</code>.</li>
</ol>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Ad-Hoc

**Intuition**

If we see say `S[0] == 'I'`, we can always put `0` as the first element; similarly, if we see `S[0] == 'D'`, we can always put `N` as the first element.

Say we have a match for the rest of the string `S[1], S[2], ...` using `N` distinct elements.  Notice it doesn't matter what the elements are, only that they are distinct and totally ordered.  Then, putting `0` or `N` at the first character will match, and the rest of the elements (`1, 2, ..., N` or `0, 1, ..., N-1`) can use the matching we have.

**Algorithm**

Keep track of the smallest and largest element we haven't placed.  If we see an `'I'`, place the small element; otherwise place the large element.

<iframe src="https://leetcode.com/playground/Lornz86n/shared" frameBorder="0" width="100%" height="327" name="Lornz86n"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
