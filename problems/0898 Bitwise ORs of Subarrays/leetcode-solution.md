# 0898 - Bitwise ORs of Subarrays

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming, Bit Manipulation | [Leetcode](https://leetcode.com/problems/bitwise-ors-of-subarrays) | [solution](https://leetcode.com/problems/bitwise-ors-of-subarrays/solution/)


-----------

<p>We have an array <code>A</code> of non-negative integers.</p>

<p>For every (contiguous) subarray <code>B =&nbsp;[A[i], A[i+1], ..., A[j]]</code> (with <code>i &lt;= j</code>), we take the bitwise OR of all the elements in <code>B</code>, obtaining a result <font face="monospace"><code>A[i] | A[i+1] | ... | A[j]</code>.</font></p>

<p>Return the number of possible&nbsp;results.&nbsp; (Results that occur more than once are only counted once in the final answer.)</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[0]</span>
<strong>Output: </strong><span id="example-output-1">1</span>
<strong>Explanation: </strong>
There is only one possible result: 0.
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[1,1,2]</span>
<strong>Output: </strong><span id="example-output-2">3</span>
<strong>Explanation: </strong>
The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[1,2,4]</span>
<strong>Output: </strong><span id="example-output-3">6</span>
<strong>Explanation: </strong>
The possible results are 1, 2, 3, 4, 6, and 7.
</pre>
</div>
</div>
</div>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 50000</code></li>
	<li><code>0 &lt;= A[i] &lt;= 10^9</code></li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Frontier Set

**Intuition**

Let's try to speed up a brute force answer.  Evidently, the brute force approach is to calculate every result `result(i, j) = A[i] | A[i+1] | ... | A[j]`.  We can speed this up by taking note of the fact that `result(i, j+1) = result(i, j) | A[j+1]`.  Naively, this approach has time complexity $$O(N^2)$$, where $$N$$ is the length of the array.

Actually, this approach can be better than that.  At the `k`th step, say we have all the `result(i, k)` in some set `cur`.  Then we can find the next `cur` set (for `k -> k+1`) by using `result(i, k+1) = result(i, k) | A[k+1]`.

However, the number of unique values in this set `cur` is at most 32, since the list `result(k, k), result(k-1, k), result(k-2, k), ...` is monotone increasing, and any subsequent values that are different must have more 1s in it's binary representation (to a maximum of 32 ones).

**Algorithm**

In the `k`th step, we'll maintain `cur`: the set of results `A[i] | ... | A[k]` for all `i`.  These results will be included in our final answer set.

<iframe src="https://leetcode.com/playground/rDNmUE84/shared" frameBorder="0" width="100%" height="344" name="rDNmUE84"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log W)$$, where $$N$$ is the length of `A`, and $$W$$ is the maximum size of elements in `A`.

* Space Complexity:  $$O(N \log W)$$, the size of the answer.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
