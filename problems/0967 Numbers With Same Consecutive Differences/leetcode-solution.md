# 0967 - Numbers With Same Consecutive Differences

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming | [Leetcode](https://leetcode.com/problems/numbers-with-same-consecutive-differences) | [solution](https://leetcode.com/problems/numbers-with-same-consecutive-differences/solution/)


-----------

<p>Return all <strong>non-negative</strong> integers of length <code>N</code> such that the absolute difference between every two consecutive digits is <code>K</code>.</p>

<p>Note that <strong>every</strong> number in the answer <strong>must not</strong> have leading zeros <strong>except</strong> for the number <code>0</code> itself. For example, <code>01</code> has one leading zero and is invalid, but <code>0</code> is valid.</p>

<p>You may return the answer in any order.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-1-1">3</span>, K = <span id="example-input-1-2">7</span>
<strong>Output: </strong><span id="example-output-1">[181,292,707,818,929]</span>
<strong>Explanation: </strong>Note that 070 is not a valid number, because it has leading zeroes.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>N = <span id="example-input-2-1">2</span>, K = <span id="example-input-2-2">1</span>
<strong>Output: </strong><span id="example-output-2">[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]</span></pre>

<p>&nbsp;</p>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= N &lt;= 9</code></li>
	<li><code>0 &lt;= K &lt;= 9</code></li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Brute Force

**Intuition**

Let's try to write some number in the answer digit by digit.

For each digit except the first, there are at most 2 choices for that digit.  This means that there are at most $$9 * 2^8$$ possible 9 digit numbers, for example.  This is small enough to brute force.

**Algorithm**

An $$N$$ digit number is just an $$N-1$$ digit number with a final digit added.  If the $$N-1$$ digit number ends in a digit $$d$$, then the $$N$$ digit number will end in $$d-K$$ or $$d+K$$ (provided these are digits in the range $$[0,9]$$).  We store these numbers in a `Set` structure to avoid duplicates.

Also, we should be careful about leading zeroes -- only 1 digit numbers will start with `0`.

<iframe src="https://leetcode.com/playground/QMVwzekW/shared" frameBorder="0" width="100%" height="500" name="QMVwzekW"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(2^N)$$.

* Space Complexity:  $$O(2^N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
