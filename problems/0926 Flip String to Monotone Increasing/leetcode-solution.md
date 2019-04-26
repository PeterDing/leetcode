# 0926 - Flip String to Monotone Increasing

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array | [Leetcode](https://leetcode.com/problems/flip-string-to-monotone-increasing) | [solution](https://leetcode.com/problems/flip-string-to-monotone-increasing/solution/)


-----------

<p>A string of <code>&#39;0&#39;</code>s and <code>&#39;1&#39;</code>s is <em>monotone increasing</em> if it consists of some number of <code>&#39;0&#39;</code>s (possibly 0), followed by some number of <code>&#39;1&#39;</code>s (also possibly 0.)</p>

<p>We are given a string <code>S</code> of <code>&#39;0&#39;</code>s and <code>&#39;1&#39;</code>s, and we may flip any <code>&#39;0&#39;</code> to a <code>&#39;1&#39;</code> or a <code>&#39;1&#39;</code> to a <code>&#39;0&#39;</code>.</p>

<p>Return the minimum number of flips to make <code>S</code>&nbsp;monotone increasing.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;00110&quot;</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>We flip the last digit to get 00111.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">&quot;010110&quot;</span>
<strong>Output: </strong><span id="example-output-2">2</span>
<strong>Explanation: </strong>We flip to get 011111, or alternatively 000111.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">&quot;00011000&quot;</span>
<strong>Output: </strong><span id="example-output-3">2</span>
<strong>Explanation: </strong>We flip to get 00000000.
</pre>

<p>&nbsp;</p>

<p><strong><span>Note:</span></strong></p>

<ol>
	<li><code>1 &lt;= S.length &lt;= 20000</code></li>
	<li><code>S</code> only consists of <code>&#39;0&#39;</code> and <code>&#39;1&#39;</code> characters.</li>
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
#### Approach 1: Prefix Sums

**Intuition**

For say a 5 digit string, the answer is either `'00000'`, `'00001'`, `'00011'`, `'00111'`, `'01111'`, or `'11111'`.  Let's try to calculate the cost of switching to that answer.  The answer has two halves, a left (zero) half, and a right (one) half.

Evidently, it comes down to a question of knowing, for each candidate half: how many ones are in the left half, and how many zeros are in the right half.

We can use prefix sums.  Say `P[i+1] = A[0] + A[1] + ... + A[i]`, where `A[i] = 1` if `S[i] == '1'`, else `A[i] = 0`.  We can calculate `P` in linear time.

Then if we want `x` zeros followed by `N-x` ones, there are `P[x]` ones in the start that must be flipped, plus `(N-x) - (P[N] - P[x])` zeros that must be flipped.  The last calculation comes from the fact that there are `P[N] - P[x]` ones in the later segment of length `N-x`, but we want the number of zeros.

**Algorithm**

For example, with `S = "010110"`:  we have `P = [0, 0, 1, 1, 2, 3, 3]`.  Now say we want to evaluate having `x=3` zeros.

There are `P[3] = 1` ones in the first 3 characters, and `P[6] - P[3] = 2` ones in the later `N-x = 3` characters.

So, there is `(N-x) - (P[N] - P[x]) = 1` zero in the later `N-x` characters.

We take the minimum among all candidate answers to arrive at the final answer.

<iframe src="https://leetcode.com/playground/AoUF2isa/shared" frameBorder="0" width="100%" height="310" name="AoUF2isa"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `S`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
