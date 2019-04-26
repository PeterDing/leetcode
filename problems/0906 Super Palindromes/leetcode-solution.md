# 0906 - Super Palindromes

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Math | [Leetcode](https://leetcode.com/problems/super-palindromes) | [solution](https://leetcode.com/problems/super-palindromes/solution/)


-----------

<p>Let&#39;s say a positive integer is a&nbsp;<em>superpalindrome</em>&nbsp;if it is a palindrome, and it is also the square of a palindrome.</p>

<p>Now, given two positive&nbsp;integers <code>L</code> and <code>R</code> (represented as strings), return the number of superpalindromes in the inclusive range <code>[L, R]</code>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>L = <span id="example-input-1-1">&quot;4&quot;</span>, R = <span id="example-input-1-2">&quot;1000&quot;</span>
<strong>Output: </strong>4
<span><strong>Explanation</strong>: </span>4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= len(L) &lt;= 18</code></li>
	<li><code>1 &lt;= len(R) &lt;= 18</code></li>
	<li><code>L</code> and <code>R</code> are strings representing integers in the range <code>[1, 10^18)</code>.</li>
	<li><code>int(L) &lt;= int(R)</code></li>
</ol>

<div>
<p>&nbsp;</p>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Mathematical

**Intuition**

Say $$P = R^2$$ is a superpalindrome.

Because $$R$$ is a palindrome, the first half of the digits in $$R$$ determine $$R$$ up to two possibilities.  We can iterate through these digits: let $$k$$ be the first half of the digits in $$R$$.  For example, if $$k = 1234$$, then $$R = 1234321$$ or $$R = 12344321$$.  Each possibility has either an odd or an even number of digits in $$R$$.

Notice because $$P < 10^{18}$$, $$R < (10^{18})^{\frac{1}{2}} = 10^9$$, and $$R = k \| k'$$ (concatenation), where $$k'$$ is $$k$$ reversed (and also possibly truncated by one digit); so that $$k < 10^5 = \small\text{MAGIC}$$, our magic constant.

**Algorithm**

For each $$1 \leq k < \small\text{MAGIC}$$, let's create the associated palindrome $$R$$, and check whether $$R^2$$ is a palindrome.

We should handle the odd and even possibilities separately, as we would like to break early so as not to do extra work.

To check whether an integer is a palindrome, we could check whether it is equal to its reverse.  To create the reverse of an integer, we can do it digit by digit.

<iframe src="https://leetcode.com/playground/ZRTHqoUW/shared" frameBorder="0" width="100%" height="500" name="ZRTHqoUW"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(W^{\frac{1}{4}} * \log W)$$, where $$W = 10^{18}$$ is our upper limit for $$R$$.  The $$\log W$$ term comes from checking whether each candidate is the root of a palindrome.

* Space Complexity:  $$O(\log W)$$, the space used to create the candidate palindrome.
<br />
<br />


---

Analysis written by: [@awice](https://leetcode.com/awice).
