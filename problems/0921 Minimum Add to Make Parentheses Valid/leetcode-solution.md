# 0921 - Minimum Add to Make Parentheses Valid

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Stack, Greedy | [Leetcode](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid) | [solution](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/solution/)


-----------

<p>Given a string&nbsp;<code>S</code> of <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code> parentheses, we add the minimum number of parentheses ( <code>&#39;(&#39;</code> or <code>&#39;)&#39;</code>, and in any positions ) so that the resulting parentheses string is valid.</p>

<p>Formally, a parentheses string is valid if and only if:</p>

<ul>
	<li>It is the empty string, or</li>
	<li>It can be written as <code>AB</code>&nbsp;(<code>A</code> concatenated with <code>B</code>), where <code>A</code> and <code>B</code> are valid strings, or</li>
	<li>It can be written as <code>(A)</code>, where <code>A</code> is a valid string.</li>
</ul>

<p>Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;())&quot;</span>
<strong>Output: </strong><span id="example-output-1">1</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;(((&quot;</span>
<strong>Output: </strong><span id="example-output-2">3</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">&quot;()&quot;</span>
<strong>Output: </strong><span id="example-output-3">0</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">&quot;()))((&quot;</span>
<strong>Output: </strong><span id="example-output-4">4</span></pre>

<p>&nbsp;</p>
</div>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>S.length &lt;= 1000</code></li>
	<li><code>S</code> only consists of <code>&#39;(&#39;</code> and <code>&#39;)&#39;</code> characters.</li>
</ol>

<div>
<div>
<div>
<div>&nbsp;</div>
</div>
</div>
</div>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Balance

**Intuition and Algorithm**

Keep track of the *balance* of the string: the number of `'('`'s minus the number of `')'`'s.  A string is valid if its balance is 0, plus every prefix has non-negative balance.

The above idea is common with matching brackets problems, but could be difficult to find if you haven't seen it before.

Now, consider the balance of every prefix of `S`.  If it is ever negative (say, -1), we must add a '(' bracket.  Also, if the balance of `S` is positive (say, `+B`), we must add `B` ')' brackets at the end.

<iframe src="https://leetcode.com/playground/mbE7BCSV/shared" frameBorder="0" width="100%" height="310" name="mbE7BCSV"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
