# 0693 - Binary Number with Alternating Bits

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Bit Manipulation | [Leetcode](https://leetcode.com/problems/binary-number-with-alternating-bits) | [solution](https://leetcode.com/problems/binary-number-with-alternating-bits/solution/)


-----------

<p>Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 5
<b>Output:</b> True
<b>Explanation:</b>
The binary representation of 5 is: 101
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> 7
<b>Output:</b> False
<b>Explanation:</b>
The binary representation of 7 is: 111.
</pre>
</p>

<p><b>Example 3:</b><br />
<pre>
<b>Input:</b> 11
<b>Output:</b> False
<b>Explanation:</b>
The binary representation of 11 is: 1011.
</pre>
</p>

<p><b>Example 4:</b><br />
<pre>
<b>Input:</b> 10
<b>Output:</b> True
<b>Explanation:</b>
The binary representation of 10 is: 1010.
</pre>
</p>

-----------


## Similar Problems

- [Easy] [Number of 1 Bits](number-of-1-bits)




## Solution:

[TOC]

#### Approach #1: Convert to String [Accepted]

**Intuition and Algorithm**

Let's convert the given number into a string of binary digits.  Then, we should simply check that no two adjacent digits are the same.

<iframe src="https://leetcode.com/playground/79o5Wvyy/shared" frameBorder="0" name="79o5Wvyy" width="100%" height="241"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(1)$$.  For arbitrary inputs, we do $$O(w)$$ work, where $$w$$ is the number of bits in `n`.  However, $$w \leq 32$$.

* Space complexity: $$O(1)$$, or alternatively $$O(w)$$.

---

#### Approach #2: Divide By Two [Accepted]

**Intuition and Algorithm**

We can get the last bit and the rest of the bits via `n % 2` and `n // 2` operations.  Let's remember `cur`, the last bit of `n`.  If the last bit ever equals the last bit of the remaining, then two adjacent bits have the same value, and the answer is `False`.  Otherwise, the answer is `True`.

Also note that instead of `n % 2` and `n // 2`, we could have used operators `n & 1` and `n >>= 1` instead.

<iframe src="https://leetcode.com/playground/oFAELrSA/shared" frameBorder="0" name="oFAELrSA" width="100%" height="258"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(1)$$.  For arbitrary inputs, we do $$O(w)$$ work, where $$w$$ is the number of bits in `n`.  However, $$w \leq 32$$.

* Space complexity: $$O(1)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice)
