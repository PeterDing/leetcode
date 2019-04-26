# 0833 - Find And Replace in String

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String | [Leetcode](https://leetcode.com/problems/find-and-replace-in-string) | [solution](https://leetcode.com/problems/find-and-replace-in-string/solution/)


-----------

<p>To some string <code>S</code>, we will perform some&nbsp;replacement&nbsp;operations that replace groups of letters with new ones (not necessarily the same size).</p>

<p>Each replacement operation has <code>3</code> parameters: a starting index <code>i</code>, a source word&nbsp;<code>x</code>&nbsp;and a target word&nbsp;<code>y</code>.&nbsp; The rule is that if <code><font face="monospace">x</font></code>&nbsp;starts at position <code>i</code>&nbsp;in the <strong>original</strong> <strong>string</strong> <strong><code>S</code></strong>, then we will replace that occurrence of&nbsp;<code>x</code>&nbsp;with&nbsp;<code>y</code>.&nbsp; If not, we do nothing.</p>

<p>For example, if we have&nbsp;<code>S = &quot;abcd&quot;</code>&nbsp;and we have some replacement operation&nbsp;<code>i = 2, x = &quot;cd&quot;, y = &quot;ffff&quot;</code>, then because&nbsp;<code>&quot;cd&quot;</code>&nbsp;starts at position <code><font face="monospace">2</font></code>&nbsp;in the original string <code>S</code>, we will replace it with <code>&quot;ffff&quot;</code>.</p>

<p>Using another example on <code>S = &quot;abcd&quot;</code>, if we have both the replacement operation <code>i = 0, x = &quot;ab&quot;, y = &quot;eee&quot;</code>, as well as another replacement operation&nbsp;<code>i = 2, x = &quot;ec&quot;, y = &quot;ffff&quot;</code>, this second operation does nothing because in the original string&nbsp;<code>S[2] = &#39;c&#39;</code>, which doesn&#39;t match&nbsp;<code>x[0] = &#39;e&#39;</code>.</p>

<p>All these operations occur simultaneously.&nbsp; It&#39;s guaranteed that there won&#39;t be any overlap in replacement: for example,&nbsp;<code>S = &quot;abc&quot;, indexes = [0, 1],&nbsp;sources = [&quot;ab&quot;,&quot;bc&quot;]</code> is not a valid test case.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = &quot;abcd&quot;, indexes = [0,2], sources = [&quot;a&quot;,&quot;cd&quot;], targets = [&quot;eee&quot;,&quot;ffff&quot;]
<strong>Output: </strong>&quot;eeebffff&quot;
<strong>Explanation:</strong> &quot;a&quot; starts at index 0 in S, so it&#39;s replaced by &quot;eee&quot;.
&quot;cd&quot; starts at index 2 in S, so it&#39;s replaced by &quot;ffff&quot;.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>S = &quot;abcd&quot;, indexes = [0,2], sources = [&quot;ab&quot;,&quot;ec&quot;], targets = [&quot;eee&quot;,&quot;ffff&quot;]
<strong>Output: </strong>&quot;eeecd&quot;
<strong>Explanation:</strong> &quot;ab&quot; starts at index 0 in S, so it&#39;s replaced by &quot;eee&quot;. 
&quot;ec&quot; doesn&#39;t starts at index 2 in the <strong>original</strong> S, so we do nothing.
</pre>

<p>Notes:</p>

<ol>
	<li><code>0 &lt;=&nbsp;indexes.length =&nbsp;sources.length =&nbsp;targets.length &lt;= 100</code></li>
	<li><code>0&nbsp;&lt;&nbsp;indexes[i]&nbsp;&lt; S.length &lt;= 1000</code></li>
	<li>All characters in given inputs are lowercase letters.</li>
</ol>

<p>&nbsp;</p>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Direct [Accepted]

**Intuition and Algorithm**

We showcase two different approaches.  In both approaches, we build some answer string `ans`, that starts as `S`.  Our main motivation in these approaches is to be able to identify and handle when a given replacement operation does nothing.

In *Java*, the idea is to build an array `match` that tells us `match[ix] = j` whenever `S[ix]` is the head of a successful replacement operation `j`: that is, whenever `S[ix:].startswith(sources[j])`.

After, we build the answer using this match array.  For each index `ix` in `S`, we can use `match` to check whether `S[ix]` is being replaced or not.  We repeatedly either write the next character `S[ix]`, or groups of characters `targets[match[ix]]`, depending on the value of `match[ix]`.

In *Python*, we sort our replacement jobs `(i, x, y)` in reverse order.  If `S[i:].startswith(x)`, then we can replace that section `S[i:i+len(x)]` with the target `y`.  We used a reverse order so that edits to `S` do not interfere with the rest of the queries.

<iframe src="https://leetcode.com/playground/2qLJpytD/shared" frameBorder="0" width="100%" height="480" name="2qLJpytD"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(NQ)$$, where $$N$$ is the length of `S`, and we have $$Q$$ replacement operations.  (Our complexity could be faster with a more accurate implementation, but it isn't necessary.)

* Space Complexity: $$O(N)$$, if we consider `targets[i].length <= 100` as a constant bound.

---

Analysis written by: [@awice](https://leetcode.com/awice).
