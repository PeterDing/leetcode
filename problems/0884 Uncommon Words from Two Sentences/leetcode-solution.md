# 0884 - Uncommon Words from Two Sentences

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Hash Table | [Leetcode](https://leetcode.com/problems/uncommon-words-from-two-sentences) | [solution](https://leetcode.com/problems/uncommon-words-from-two-sentences/solution/)


-----------

<p>We are given two sentences <code>A</code> and <code>B</code>.&nbsp; (A <em>sentence</em>&nbsp;is a string of space separated words.&nbsp; Each <em>word</em> consists only of lowercase letters.)</p>

<p>A word is <em>uncommon</em>&nbsp;if it appears exactly once in one of the sentences, and does not appear in the other sentence.</p>

<p>Return a list of all uncommon words.&nbsp;</p>

<p>You may return the list in any order.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">&quot;this apple is sweet&quot;</span>, B = <span id="example-input-1-2">&quot;this apple is sour&quot;</span>
<strong>Output: </strong><span id="example-output-1">[&quot;sweet&quot;,&quot;sour&quot;]</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-2-1">&quot;apple apple&quot;</span>, B = <span id="example-input-2-2">&quot;banana&quot;</span>
<strong>Output: </strong><span id="example-output-2">[&quot;banana&quot;]</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt;= 200</code></li>
	<li><code>0 &lt;= B.length &lt;= 200</code></li>
	<li><code>A</code> and <code>B</code> both contain only spaces and lowercase letters.</li>
</ol>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Counting

**Intuition and Algorithm**

Every uncommon word occurs exactly once in total.  We can count the number of occurrences of every word, then return ones that occur exactly once.

<iframe src="https://leetcode.com/playground/YwdvfZv6/shared" frameBorder="0" width="100%" height="327" name="YwdvfZv6"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(M + N)$$, where $$M, N$$ are the lengths of `A` and `B` respectively.

* Space Complexity:  $$O(M + N)$$, the space used by `count`.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
