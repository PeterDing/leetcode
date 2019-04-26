# 0650 - 2 Keys Keyboard

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming | [Leetcode](https://leetcode.com/problems/2-keys-keyboard) | [solution](https://leetcode.com/problems/2-keys-keyboard/solution/)


-----------

<p>Initially on a notepad only one character &#39;A&#39; is present. You can perform two operations on this notepad for each step:</p>

<ol>
	<li><code>Copy All</code>: You can copy all the characters present on the notepad (partial copy is not allowed).</li>
	<li><code>Paste</code>: You can paste the characters which are copied <b>last time</b>.</li>
</ol>

<p>&nbsp;</p>

<p>Given a number <code>n</code>. You have to get <b>exactly</b> <code>n</code> &#39;A&#39; on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get <code>n</code> &#39;A&#39;.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 3
<b>Output:</b> 3
<b>Explanation:</b>
Intitally, we have one character &#39;A&#39;.
In step 1, we use <b>Copy All</b> operation.
In step 2, we use <b>Paste</b> operation to get &#39;AA&#39;.
In step 3, we use <b>Paste</b> operation to get &#39;AAA&#39;.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ol>
	<li>The <code>n</code> will be in the range [1, 1000].</li>
</ol>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Medium] [4 Keys Keyboard](4-keys-keyboard)

- [Medium] [Broken Calculator](broken-calculator)




## Solution:

[TOC]

---
#### Approach #1: Prime Factorization [Accepted]

**Intuition**

We can break our moves into groups of `(copy, paste, ..., paste)`.  Let `C` denote copying and `P` denote pasting.  Then for example, in the sequence of moves `CPPCPPPPCP`, the groups would be `[CPP][CPPPP][CP]`.

Say these groups have lengths `g_1, g_2, ...`.  After parsing the first group, there are `g_1` `'A'`s.  After parsing the second group, there are `g_1 * g_2` `'A'`s, and so on.  At the end, there are `g_1 * g_2 * ... * g_n` `'A'`s.

We want exactly `N = g_1 * g_2 * ... * g_n`.  If any of the `g_i` are composite, say `g_i = p * q`, then we can split this group into two groups (the first of which has one copy followed by `p-1` pastes, while the second group having one copy and `q-1` pastes).

Such a split never uses more moves: we use `p+q` moves when splitting, and `pq` moves previously.  As `p+q <= pq` is equivalent to `1 <= (p-1)(q-1)`, which is true as long as `p >= 2` and `q >= 2`.

**Algorithm**
By the above argument, we can suppose `g_1, g_2, ...` is the prime factorization of `N`, and the answer is therefore the sum of these prime factors.

<iframe src="https://leetcode.com/playground/U88jzmPG/shared" frameBorder="0" width="100%" height="276" name="U88jzmPG"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(\sqrt{N})$$.  When `N` is the square of a prime, our loop does $$O(\sqrt{N})$$ steps.

* Space Complexity: $$O(1)$$, the space used by `ans` and `d`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
