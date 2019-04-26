# 0880 - Decoded String at Index

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Stack | [Leetcode](https://leetcode.com/problems/decoded-string-at-index) | [solution](https://leetcode.com/problems/decoded-string-at-index/solution/)


-----------

<p>An encoded string <code>S</code> is given.&nbsp; To find and write the <em>decoded</em> string to a tape, the encoded string is read <strong>one character at a time</strong>&nbsp;and the following steps are taken:</p>

<ul>
	<li>If the character read is a letter, that letter is written onto the tape.</li>
	<li>If the character read is a digit (say <code>d</code>), the entire current tape is repeatedly written&nbsp;<code>d-1</code>&nbsp;more times in total.</li>
</ul>

<p>Now for some encoded string <code>S</code>, and an index <code>K</code>, find and return the <code>K</code>-th letter (1 indexed) in the decoded string.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-1-1">&quot;leet2code3&quot;</span>, K = <span id="example-input-1-2">10</span>
<strong>Output: </strong><span id="example-output-1">&quot;o&quot;</span>
<strong>Explanation: </strong>
The decoded string is &quot;leetleetcodeleetleetcodeleetleetcode&quot;.
The 10th letter in the string is &quot;o&quot;.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-2-1">&quot;ha22&quot;</span>, K = <span id="example-input-2-2">5</span>
<strong>Output: </strong><span id="example-output-2">&quot;h&quot;</span>
<strong>Explanation: </strong>
The decoded string is &quot;hahahaha&quot;.  The 5th letter is &quot;h&quot;.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-3-1">&quot;a2345678999999999999999&quot;</span>, K = <span id="example-input-3-2">1</span>
<strong>Output: </strong><span id="example-output-3">&quot;a&quot;</span>
<strong>Explanation: </strong>
The decoded string is &quot;a&quot; repeated 8301530446056247680 times.  The 1st letter is &quot;a&quot;.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= S.length &lt;= 100</code></li>
	<li><code>S</code>&nbsp;will only contain lowercase letters and digits <code>2</code> through <code>9</code>.</li>
	<li><code>S</code>&nbsp;starts with a letter.</li>
	<li><code>1 &lt;= K &lt;= 10^9</code></li>
	<li>The decoded string is guaranteed to have less than <code>2^63</code> letters.</li>
</ol>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Work Backwards

**Intuition**

If we have a decoded string like `appleappleappleappleappleapple` and an index like `K = 24`, the answer is the same if `K = 4`.

In general, when a decoded string is equal to some word with `size` length repeated some number of times (such as `apple` with `size = 5` repeated 6 times), the answer is the same for the index `K` as it is for the index `K % size`.

We can use this insight by working backwards, keeping track of the size of the decoded string.  Whenever the decoded string would equal some `word` repeated `d` times, we can reduce `K` to `K % (word.length)`.

**Algorithm**

First, find the length of the decoded string.  After, we'll work backwards, keeping track of `size`: the length of the decoded string after parsing symbols `S[0], S[1], ..., S[i]`.

If we see a digit `S[i]`, it means the size of the decoded string after parsing `S[0], S[1], ..., S[i-1]` will be `size / Integer(S[i])`.  Otherwise, it will be `size - 1`.


<iframe src="https://leetcode.com/playground/HGcLTehJ/shared" frameBorder="0" width="100%" height="500" name="HGcLTehJ"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
