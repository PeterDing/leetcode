# 0869 - Reordered Power of 2

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Math | [Leetcode](https://leetcode.com/problems/reordered-power-of-2) | [solution](https://leetcode.com/problems/reordered-power-of-2/solution/)


-----------

<p>Starting with a positive integer <code>N</code>, we reorder the digits in any order (including the original order) such that the leading digit is not zero.</p>

<p>Return <code>true</code>&nbsp;if and only if we can do this in a way such that the resulting number is a power of 2.</p>

<p>&nbsp;</p>

<ol>
</ol>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">1</span>
<strong>Output: </strong><span id="example-output-1">true</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">10</span>
<strong>Output: </strong><span id="example-output-2">false</span>
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">16</span>
<strong>Output: </strong><span id="example-output-3">true</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">24</span>
<strong>Output: </strong><span id="example-output-4">false</span>
</pre>

<div>
<p><strong>Example 5:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-5-1">46</span>
<strong>Output: </strong><span id="example-output-5">true</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 10^9</code></li>
</ol>
</div>
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
#### Approach 1: Permutations

**Intuition**

For each permutation of the digits of `N`, let's check if that permutation is a power of 2.

**Algorithm**

This approach has two steps: how will we generate the permutations of the digits, and how will we check that the permutation represents a power of 2?

To generate permutations of the digits, we place any digit into the first position (`start = 0`), then any of the remaining digits into the second position (`start = 1`), and so on.  In Python, we can use the builtin function `itertools.permutations`.

To check whether a permutation represents a power of 2, we check that there is no leading zero, and divide out all factors of 2.  If the result is `1` (that is, it contained no other factors besides `2`), then it was a power of 2.  In Python, we can use the check `bin(N).count('1') == 1`.


<iframe src="https://leetcode.com/playground/jfG2dxr5/shared" frameBorder="0" width="100%" height="500" name="jfG2dxr5"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O((\log N)! * \log N)$$.  Note that $$\log N$$ is the number of digits in the binary representation of $$N$$.  For each of $$(\log N)!$$ permutations of the digits of $$N$$, we need to check that it is a power of 2 in $$O(\log N)$$ time.

* Space Complexity:  $$O(\log N)$$, the space used by `A` (or `cand` in Python).
<br />
<br />


---
#### Approach 2: Counting

**Intuition and Algorithm**

We can check whether two numbers have the same digits by comparing the *count* of their digits.  For example, 338 and 833 have the same digits because they both have exactly two 3's and one 8.

Since $$N$$ could only be a power of 2 with 9 digits or less (namely, $$2^0, 2^1, \cdots, 2^29$$), we can just check whether $$N$$ has the same digits as any of these possibilities.

<iframe src="https://leetcode.com/playground/ZV2nPKdj/shared" frameBorder="0" width="100%" height="395" name="ZV2nPKdj"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(\log^2 N)$$.  There are $$\log N$$ different candidate powers of 2, and each comparison has $$O(\log N)$$ time complexity.

* Space Complexity:  $$O(\log N)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
