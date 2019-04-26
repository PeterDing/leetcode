# 0972 - Equal Rational Numbers

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Math | [Leetcode](https://leetcode.com/problems/equal-rational-numbers) | [solution](https://leetcode.com/problems/equal-rational-numbers/solution/)


-----------

<p>Given two strings <code>S</code> and <code>T</code>, each of which represents a non-negative rational number, return <strong>True</strong> if and only if they represent the same number. The strings may use parentheses to denote the repeating part of the rational number.</p>

<p>In general a rational number can be represented using up to&nbsp;three parts: an&nbsp;<em>integer part</em>, a&nbsp;<em>non-repeating part,</em> and a&nbsp;<em>repeating part</em>. The number will be represented&nbsp;in one of the following three ways:</p>

<ul>
	<li><code>&lt;IntegerPart&gt;</code> (e.g. 0, 12, 123)</li>
	<li><code>&lt;IntegerPart&gt;&lt;.&gt;&lt;NonRepeatingPart&gt;</code> &nbsp;(e.g. 0.5, 1., 2.12, 2.0001)</li>
	<li><code>&lt;IntegerPart&gt;&lt;.&gt;&lt;NonRepeatingPart&gt;&lt;(&gt;&lt;RepeatingPart&gt;&lt;)&gt;</code> (e.g. 0.1(6), 0.9(9), 0.00(1212))</li>
</ul>

<p>The repeating portion of a decimal expansion is conventionally denoted within a pair of round brackets.&nbsp; For example:</p>

<p>1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)</p>

<p>Both 0.1(6) or 0.1666(6) or 0.166(66) are correct representations of 1 / 6.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-1-1">&quot;0.(52)&quot;</span>, T = <span id="example-input-1-2">&quot;0.5(25)&quot;</span>
<strong>Output: </strong><span id="example-output-1">true</span>
<strong>Explanation:
</strong>Because &quot;0.(52)&quot; represents 0.52525252..., and &quot;0.5(25)&quot; represents 0.52525252525..... , the strings represent the same number.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-2-1">&quot;0.1666(6)&quot;</span>, T = <span id="example-input-2-2">&quot;0.166(66)&quot;</span>
<strong>Output: </strong><span id="example-output-2">true</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong>S = <span id="example-input-3-1">&quot;0.9(9)&quot;</span>, T = <span id="example-input-3-2">&quot;1.&quot;</span>
<strong>Output: </strong><span id="example-output-3">true</span>
<strong>Explanation: </strong>
&quot;0.9(9)&quot; represents 0.999999999... repeated forever, which equals 1.  [<a href="https://en.wikipedia.org/wiki/0.999..." target="_blank">See this link for an explanation.</a>]
&quot;1.&quot; represents the number 1, which is formed correctly: (IntegerPart) = &quot;1&quot; and (NonRepeatingPart) = &quot;&quot;.</pre>

<p>&nbsp;</p>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li>Each part consists only of digits.</li>
	<li>The <code>&lt;IntegerPart&gt;</code>&nbsp;will&nbsp;not begin with 2 or more zeros.&nbsp; (There is no other restriction on the digits of each part.)</li>
	<li><code>1 &lt;= &lt;IntegerPart&gt;.length &lt;= 4 </code></li>
	<li><code>0 &lt;= &lt;NonRepeatingPart&gt;.length &lt;= 4 </code></li>
	<li><code>1 &lt;= &lt;RepeatingPart&gt;.length &lt;= 4</code></li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Fraction Class

**Intuition**

As both numbers represent a fraction, we need a fraction class to handle fractions.  It should help us add two fractions together, keeping the answer in lowest terms.

**Algorithm**

We need to make sense of the fraction we are given.  The hard part is the repeating part.

Say we have a string like `S = "0.(12)"`.  It represents (for $$r = \frac{1}{100}$$):

$$
S = \frac{12}{100} + \frac{12}{10000} + \frac{12}{10^6} + \frac{12}{10^8} + \frac{12}{10^{10}} + \cdots
$$

$$
S = 12 * (r + r^2 + r^3 + \cdots)
$$

$$
S = 12 * \frac{r}{1-r}
$$

as the sum $$(r + r^2 + r^3 + \cdots)$$ is a geometric sum.

In general, for a repeating part $$x$$ with length $$k$$, we have $$r = 10^{-k}$$ and the contribution is $$\frac{xr}{1-r}$$.

The other two parts are easier, as it is just a literal interpretation of the value.

<iframe src="https://leetcode.com/playground/hvAK7yRs/shared" frameBorder="0" width="100%" height="500" name="hvAK7yRs"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(1)$$, if we take the length of $$S, T$$ as $$O(1)$$.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
