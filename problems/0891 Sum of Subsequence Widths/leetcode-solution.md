# 0891 - Sum of Subsequence Widths

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Array, Math | [Leetcode](https://leetcode.com/problems/sum-of-subsequence-widths) | [solution](https://leetcode.com/problems/sum-of-subsequence-widths/solution/)


-----------

<p>Given an array of integers <code>A</code>, consider all non-empty subsequences of <code>A</code>.</p>

<p>For any sequence S, let the&nbsp;<em>width</em>&nbsp;of S be the difference between the maximum and minimum element of S.</p>

<p>Return the sum of the widths of all subsequences of A.&nbsp;</p>

<p>As the answer may be very large, <strong>return the answer modulo 10^9 + 7</strong>.</p>

<div>
<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[2,1,3]</span>
<strong>Output: </strong><span id="example-output-1">6</span>
<strong>Explanation:
</strong>Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
The sum of these widths is 6.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ul>
	<li><code>1 &lt;= A.length &lt;= 20000</code></li>
	<li><code>1 &lt;= A[i] &lt;= 20000</code></li>
</ul>
</div>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Mathematical

**Intuition**

Let's try to count the number of subsequences with minimum `A[i]` and maximum `A[j]`.

**Algorithm**

We can sort the array as it doesn't change the answer.  After sorting the array, this allows us to know that the number of subsequences with minimum `A[i]` and maximum `A[j]` is $$2^{j-i-1}$$.  Hence, the desired answer is:

$$
\sum\limits_{j > i} (2^{j-i-1}) (A_j - A_i)
$$

$$
= \big( \sum\limits_{i = 0}^{n-2} \sum\limits_{j = i+1}^{n-1} (2^{j-i-1}) (A_j) \big) - \big( \sum\limits_{i = 0}^{n-2} \sum\limits_{j = i+1}^{n-1} (2^{j-i-1}) (A_i) \big)
$$

$$
= \big( (2^0 A_1 + 2^1 A_2 + 2^2 A_3 + \cdots) + (2^0 A_2 + 2^1 A_3 + \cdots) + (2^0 A_3 + 2^1 A_4 + \cdots) + \cdots \big)
$$
$$
 - \big( \sum\limits_{i = 0}^{n-2} (2^0 + 2^1 + \cdots + 2^{N-i-2}) (A_i) \big)
$$

$$
= \big( \sum\limits_{j = 1}^{n-1} (2^j - 1) A_j \big) - \big( \sum\limits_{i = 0}^{n-2} (2^{N-i-1} - 1) A_i \big)
$$

$$
= \sum\limits_{i = 0}^{n-1} \big(((2^i - 1) A_i) - ((2^{N-i-1} - 1) A_i)\big)
$$

$$
= \sum\limits_{i = 0}^{n-1} (2^i - 2^{N-i-1}) A_i
$$

<iframe src="https://leetcode.com/playground/DmYZUfzN/shared" frameBorder="0" width="100%" height="361" name="DmYZUfzN"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$, the space used by `pow2`.  (We can improve this to $$O(1)$$ space by calculating these powers on the fly.)
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
