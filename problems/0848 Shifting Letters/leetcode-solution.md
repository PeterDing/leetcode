# 0848 - Shifting Letters

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String | [Leetcode](https://leetcode.com/problems/shifting-letters) | [solution](https://leetcode.com/problems/shifting-letters/solution/)


-----------

<p>We have a string <code>S</code> of lowercase letters, and an integer array <code>shifts</code>.</p>

<p>Call the <em>shift</em> of a letter, the next letter in the alphabet, (wrapping around so that <code>&#39;z&#39;</code> becomes <code>&#39;a&#39;</code>).&nbsp;</p>

<p>For example, <code>shift(&#39;a&#39;) = &#39;b&#39;</code>, <code>shift(&#39;t&#39;) = &#39;u&#39;</code>, and <code>shift(&#39;z&#39;) = &#39;a&#39;</code>.</p>

<p>Now for each <code>shifts[i] = x</code>, we want to shift the first <code>i+1</code>&nbsp;letters of <code>S</code>, <code>x</code> times.</p>

<p>Return the final string&nbsp;after all such shifts to <code>S</code> are applied.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = &quot;abc&quot;, shifts = [3,5,9]
<strong>Output: </strong>&quot;rpl&quot;
<strong>Explanation: </strong>
We start with &quot;abc&quot;.
After shifting the first 1 letters of S by 3, we have &quot;dbc&quot;.
After shifting the first 2 letters of S by 5, we have &quot;igc&quot;.
After shifting the first 3 letters of S by 9, we have &quot;rpl&quot;, the answer.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= S.length = shifts.length &lt;= 20000</code></li>
	<li><code>0 &lt;= shifts[i] &lt;= 10 ^ 9</code></li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Prefix Sum [Accepted]

**Intuition**

Let's ask how many times the `i`th character is shifted.

**Algorithm**

The `i`th character is shifted `shifts[i] + shifts[i+1] + ... + shifts[shifts.length - 1]` times.  That's because only operations at the `i`th operation and after, affect the `i`th character.

Let `X` be the number of times the current `i`th character is shifted.  Then the next character `i+1` is shifted `X - shifts[i]` times.

For example, if `S.length = 4` and `S[0]` is shifted `X = shifts[0] + shifts[1] + shifts[2] + shifts[3]` times, then `S[1]` is shifted `shifts[1] + shifts[2] + shifts[3]` times, `S[2]` is shifted `shifts[2] + shifts[3]` times, and so on.

In general, we need to do `X -= shifts[i]` to maintain the correct value of `X` as we increment `i`.

<iframe src="https://leetcode.com/playground/eh9zG8Q2/shared" frameBorder="0" width="100%" height="327" name="eh9zG8Q2"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S` (and `shifts`).

* Space Complexity:  $$O(N)$$, the space needed to output the answer.

---

Analysis written by: [@awice](https://leetcode.com/awice).
