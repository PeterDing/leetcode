# 0856 - Score of Parentheses

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String, Stack | [Leetcode](https://leetcode.com/problems/score-of-parentheses) | [solution](https://leetcode.com/problems/score-of-parentheses/solution/)


-----------

<p>Given a balanced parentheses string <code>S</code>, compute the score of the string based on the following rule:</p>

<ul>
	<li><code>()</code> has score 1</li>
	<li><code>AB</code> has score <code>A + B</code>, where A and B are balanced parentheses strings.</li>
	<li><code>(A)</code> has score <code>2 * A</code>, where A is a balanced parentheses string.</li>
</ul>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;()&quot;</span>
<strong>Output: </strong><span id="example-output-1">1</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;(())&quot;</span>
<strong>Output: </strong><span id="example-output-2">2</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">&quot;()()&quot;</span>
<strong>Output: </strong><span id="example-output-3">2</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">&quot;(()(()))&quot;</span>
<strong>Output: </strong><span id="example-output-4">6</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>S</code> is a balanced parentheses string, containing only <code>(</code> and <code>)</code>.</li>
	<li><code>2 &lt;= S.length &lt;= 50</code></li>
</ol>
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
#### Approach 1: Divide and Conquer

**Intuition**

Split the string into `S = A + B` where `A` and `B` are balanced parentheses strings, and `A` is the smallest possible non-empty prefix of `S`.

**Algorithm**

Call a balanced string *primitive* if it cannot be partitioned into two non-empty balanced strings.

By keeping track of `balance` (the number of `(` parentheses minus the number of `)` parentheses), we can partition `S` into primitive substrings `S = P_1 + P_2 + ... + P_n`.  Then, `score(S) = score(P_1) + score(P_2) + ... + score(P_n)`, by definition.

For each primitive substring `(S[i], S[i+1], ..., S[k])`, if the string is length 2, then the score of this string is 1.  Otherwise, it's twice the score of the substring `(S[i+1], S[i+2], ..., S[k-1])`.

<iframe src="https://leetcode.com/playground/9n8zxSrk/shared" frameBorder="0" width="100%" height="446" name="9n8zxSrk"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `S`.  An example worst case is `(((((((....)))))))`.

* Space Complexity:  $$O(N)$$, the size of the implied call stack.
<br />
<br />


---
#### Approach 2: Stack

**Intuition and Algorithm**

Every position in the string has a *depth* - some number of matching parentheses surrounding it.  For example, the dot in `(()(.()))` has depth 2, because of these parentheses: `(__(.__))`

Our goal is to maintain the score at the current depth we are on.  When we see an opening bracket, we increase our depth, and our score at the new depth is 0.  When we see a closing bracket, we add twice the score of the previous deeper part - except when counting `()`, which has a score of 1.

For example, when counting `(()(()))`, our stack will look like this:

* `[0, 0]` after parsing `(`
* `[0, 0, 0]` after `(`
* `[0, 1]` after `)`
* `[0, 1, 0]` after `(`
* `[0, 1, 0, 0]` after `(`
* `[0, 1, 1]` after `)`
* `[0, 3]` after `)`
* `[6]` after `)`

<iframe src="https://leetcode.com/playground/C2ky8oiW/shared" frameBorder="0" width="100%" height="327" name="C2ky8oiW"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.

* Space Complexity:  $$O(N)$$, the size of the stack.
<br />
<br />


---
#### Approach 3: Count Cores

**Intuition**

The final sum will be a sum of powers of 2, as every *core* (a substring `()`, with score 1) will have it's score multiplied by 2 for each exterior set of parentheses that contains that core.

**Algorithm**

Keep track of the `balance` of the string, as defined in *Approach #1*.  For every `)` that immediately follows a `(`, the answer is `1 << balance`, as `balance` is the number of exterior set of parentheses that contains this core.

<iframe src="https://leetcode.com/playground/EUsmNAS5/shared" frameBorder="0" width="100%" height="344" name="EUsmNAS5"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
