# 0816 - Ambiguous Coordinates

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | String | [Leetcode](https://leetcode.com/problems/ambiguous-coordinates) | [solution](https://leetcode.com/problems/ambiguous-coordinates/solution/)


-----------

<p>We had some 2-dimensional coordinates, like <code>&quot;(1, 3)&quot;</code> or <code>&quot;(2, 0.5)&quot;</code>.&nbsp; Then, we removed&nbsp;all commas, decimal points, and spaces, and ended up with the string&nbsp;<code>S</code>.&nbsp; Return a list of strings representing&nbsp;all possibilities for what our original coordinates could have been.</p>

<p>Our original representation never had extraneous zeroes, so we never started with numbers like &quot;00&quot;, &quot;0.0&quot;, &quot;0.00&quot;, &quot;1.0&quot;, &quot;001&quot;, &quot;00.01&quot;, or any other number that can be represented with&nbsp;less digits.&nbsp; Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like &quot;.1&quot;.</p>

<p>The final answer list can be returned in any order.&nbsp; Also note that all coordinates in the final answer&nbsp;have exactly one space between them (occurring after the comma.)</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> &quot;(123)&quot;
<strong>Output:</strong> [&quot;(1, 23)&quot;, &quot;(12, 3)&quot;, &quot;(1.2, 3)&quot;, &quot;(1, 2.3)&quot;]
</pre>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> &quot;(00011)&quot;
<strong>Output:</strong> &nbsp;[&quot;(0.001, 1)&quot;, &quot;(0, 0.011)&quot;]
<strong>Explanation:</strong> 
0.0, 00, 0001 or 00.01 are not allowed.
</pre>

<pre>
<strong>Example 3:</strong>
<strong>Input:</strong> &quot;(0123)&quot;
<strong>Output:</strong> [&quot;(0, 123)&quot;, &quot;(0, 12.3)&quot;, &quot;(0, 1.23)&quot;, &quot;(0.1, 23)&quot;, &quot;(0.1, 2.3)&quot;, &quot;(0.12, 3)&quot;]
</pre>

<pre>
<strong>Example 4:</strong>
<strong>Input:</strong> &quot;(100)&quot;
<strong>Output:</strong> [(10, 0)]
<strong>Explanation:</strong> 
1.0 is not allowed.
</pre>

<p>&nbsp;</p>

<p><strong>Note: </strong></p>

<ul>
	<li><code>4 &lt;= S.length &lt;= 12</code>.</li>
	<li><code>S[0]</code> = &quot;(&quot;, <code>S[S.length - 1]</code> = &quot;)&quot;, and the other elements in <code>S</code> are digits.</li>
</ul>

<p>&nbsp;</p>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Cartesian Product [Accepted]

**Intuition and Algorithm**

For each place to put the comma, we separate the string into two fragments.  For example, with a string like `"1234"`, we could separate it into fragments `"1" and "234"`, `"12" and "34"`, or `"123"` and `"4"`.

Then, for each fragment, we have a choice of where to put the period, to create a list `make(...)` of choices.  For example, `"123"` could be made into `"1.23"`, `"12.3"`, or `"123"`.

Because of extranneous zeroes, we should ignore possibilities where the part of the fragment to the `left` of the decimal starts with `"0"` (unless it is exactly `"0"`), and ignore possibilities where the part of the fragment to the `right` of the decimal ends with `"0"`, as these are not allowed.

Note that this process could result in an empty answer, such as for the case `S = "(000)"`.

<iframe src="https://leetcode.com/playground/Gdyt4CNE/shared" frameBorder="0" width="100%" height="463" name="Gdyt4CNE"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^3)$$, where $$N$$ is the length `S`.  We evaluate the sum $$O(\sum_k k(N-k))$$.

* Space Complexity: $$O(N^3)$$, to store the answer.

---

Analysis written by: [@awice](https://leetcode.com/awice).
