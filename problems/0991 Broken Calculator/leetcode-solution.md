# 0991 - Broken Calculator

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Math, Greedy | [Leetcode](https://leetcode.com/problems/broken-calculator) | [solution](https://leetcode.com/problems/broken-calculator/solution/)


-----------

<p>On a broken calculator that has a number showing on its display, we can perform two operations:</p>

<ul>
	<li><strong>Double</strong>: Multiply the number on the display by 2, or;</li>
	<li><strong>Decrement</strong>: Subtract 1 from the number on the display.</li>
</ul>

<p>Initially, the calculator is displaying the number <code>X</code>.</p>

<p>Return the minimum number of operations needed to display the number <code>Y</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>X = <span id="example-input-1-1">2</span>, Y = <span id="example-input-1-2">3</span>
<strong>Output: </strong><span id="example-output-1">2</span>
<strong>Explanation: </strong>Use double operation and then decrement operation {2 -&gt; 4 -&gt; 3}.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>X = <span id="example-input-2-1">5</span>, Y = <span id="example-input-2-2">8</span>
<strong>Output: </strong><span id="example-output-2">2</span>
<strong>Explanation: </strong>Use decrement and then double {5 -&gt; 4 -&gt; 8}.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>X = <span id="example-input-3-1">3</span>, Y = <span id="example-input-3-2">10</span>
<strong>Output: </strong><span id="example-output-3">3</span>
<strong>Explanation: </strong> Use double, decrement and double {3 -&gt; 6 -&gt; 5 -&gt; 10}.
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong>X = <span id="example-input-4-1">1024</span>, Y = <span id="example-input-4-2">1</span>
<strong>Output: </strong><span id="example-output-4">1023</span>
<strong>Explanation: </strong>Use decrement operations 1023 times.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= X &lt;= 10^9</code></li>
	<li><code>1 &lt;= Y &lt;= 10^9</code></li>
</ol>

-----------


## Similar Problems

- [Medium] [2 Keys Keyboard](2-keys-keyboard)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Work Backwards

**Intuition**

Instead of multiplying by 2 or subtracting 1 from `X`, we could divide by 2 (when `Y` is even) or add 1 to `Y`.

The motivation for this is that it turns out we always greedily divide by 2:

* If say `Y` is even, then if we perform 2 additions and one division, we could instead perform one division and one addition for less operations [`(Y+2) / 2` vs `Y/2 + 1`].

* If say `Y` is odd, then if we perform 3 additions and one division, we could instead perform 1 addition, 1 division, and 1 addition for less operations [`(Y+3) / 2` vs `(Y+1) / 2 + 1`].

**Algorithm**

While `Y` is larger than `X`, add 1 if it is odd, else divide by 2.  After, we need to do `X - Y` additions to reach `X`.

<iframe src="https://leetcode.com/playground/xhbtbZzk/shared" frameBorder="0" width="100%" height="293" name="xhbtbZzk"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\log Y)$$.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
