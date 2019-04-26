# 0935 - Knight Dialer

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming | [Leetcode](https://leetcode.com/problems/knight-dialer) | [solution](https://leetcode.com/problems/knight-dialer/solution/)


-----------

<p>A chess knight can move as indicated in the chess diagram below:</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2018/10/12/knight.png" style="width: 150px; height: 150px;" />&nbsp;.&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<img alt="" src="https://assets.leetcode.com/uploads/2018/10/30/keypad.png" style="width: 134px; height: 150px;" /></p>

<p>&nbsp;</p>

<p>This time, we place our chess knight on any numbered key of a phone pad (indicated above), and the knight makes <code>N-1</code> hops.&nbsp; Each hop must be from one key to another numbered key.</p>

<p>Each time it lands on a key (including the initial placement of the knight), it presses the number of that key, pressing <code>N</code> digits total.</p>

<p>How many distinct numbers can you dial in this manner?</p>

<p>Since the answer may be large, <strong>output the answer&nbsp;modulo <code>10^9 + 7</code></strong>.</p>

<p>&nbsp;</p>

<ul>
</ul>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">1</span>
<strong>Output: </strong><span id="example-output-1">10</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">2</span>
<strong>Output: </strong><span id="example-output-2">20</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">3</span>
<strong>Output: </strong><span id="example-output-3">46</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= N &lt;= 5000</code></li>
</ul>
</div>
</div>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Dynamic Programming

**Intuition**

Let `f(start, n)` be the number of ways to dial an `n` digit number, where the knight starts at square `start`.  We can create a recursion, writing this in terms of `f(x, n-1)`'s.

**Algorithm**

By hand or otherwise, have a way to query what moves are available at each square.  This implies the exact recursion for `f`.  For example, from `1` we can move to `6, 8`, so `f(1, n) = f(6, n-1) + f(8, n-1)`.

After, let's keep track of `dp[start] = f(start, n)`, and update it for each n from `1, 2, ..., N`.

At the end, the answer is `f(0, N) + f(1, N) + ... + f(9, N) = sum(dp)`.

<iframe src="https://leetcode.com/playground/EirthMi4/shared" frameBorder="0" width="100%" height="463" name="EirthMi4"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
