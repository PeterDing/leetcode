# 0844 - Backspace String Compare

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Two Pointers, Stack | [Leetcode](https://leetcode.com/problems/backspace-string-compare) | [solution](https://leetcode.com/problems/backspace-string-compare/solution/)


-----------

<p>Given two&nbsp;strings&nbsp;<code>S</code>&nbsp;and <code>T</code>,&nbsp;return if they are equal when both are typed into empty text editors. <code>#</code> means a backspace character.</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-1-1">&quot;ab#c&quot;</span>, T = <span id="example-input-1-2">&quot;ad#c&quot;</span>
<strong>Output: </strong><span id="example-output-1">true
</span><span><strong>Explanation</strong>: Both S and T become &quot;ac&quot;.</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-2-1">&quot;ab##&quot;</span>, T = <span id="example-input-2-2">&quot;c#d#&quot;</span>
<strong>Output: </strong><span id="example-output-2">true
</span><span><strong>Explanation</strong>: Both S and T become &quot;&quot;.</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-3-1">&quot;a##c&quot;</span>, T = <span id="example-input-3-2">&quot;#a#c&quot;</span>
<strong>Output: </strong><span id="example-output-3">true
</span><span><strong>Explanation</strong>: Both S and T become &quot;c&quot;.</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-4-1">&quot;a#c&quot;</span>, T = <span id="example-input-4-2">&quot;b&quot;</span>
<strong>Output: </strong><span id="example-output-4">false
</span><span><strong>Explanation</strong>: S becomes &quot;c&quot; while T becomes &quot;b&quot;.</span>
</pre>

<p><span><strong>Note</strong>:</span></p>

<ol>
	<li><code><span>1 &lt;= S.length &lt;= 200</span></code></li>
	<li><code><span>1 &lt;= T.length &lt;= 200</span></code></li>
	<li><span><code>S</code>&nbsp;and <code>T</code> only contain&nbsp;lowercase letters and <code>&#39;#&#39;</code> characters.</span></li>
</ol>

<p><strong>Follow up:</strong></p>

<ul>
	<li>Can you solve it in <code>O(N)</code> time and <code>O(1)</code> space?</li>
</ul>
</div>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Build String [Accepted]

**Intuition**

Let's individually build the result of each string (`build(S)` and `build(T)`), then compare if they are equal.

**Algorithm**

To build the result of a string `build(S)`, we'll use a stack based approach, simulating the result of each keystroke.

<iframe src="https://leetcode.com/playground/oeguUYg8/shared" frameBorder="0" width="100%" height="327" name="oeguUYg8"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(M + N)$$, where $$M, N$$ are the lengths of `S` and `T` respectively.

* Space Complexity:  $$O(M + N)$$.


---
#### Approach #2: Two Pointer [Accepted]

**Intuition**

When writing a character, it may or may not be part of the final string depending on how many backspace keystrokes occur in the future.

If instead we iterate through the string in reverse, then we will know how many backspace characters we have seen, and therefore whether the result includes our character.

**Algorithm**

Iterate through the string in reverse.  If we see a backspace character, the next non-backspace character is skipped.  If a character isn't skipped, it is part of the final answer.

See the comments in the code for more details.

<iframe src="https://leetcode.com/playground/sqdQBEmS/shared" frameBorder="0" width="100%" height="500" name="sqdQBEmS"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(M + N)$$, where $$M, N$$ are the lengths of `S` and `T` respectively.

* Space Complexity:  $$O(1)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
