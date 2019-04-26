# 0974 - Subarray Sums Divisible by K

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Hash Table | [Leetcode](https://leetcode.com/problems/subarray-sums-divisible-by-k) | [solution](https://leetcode.com/problems/subarray-sums-divisible-by-k/solution/)


-----------

<p>Given an array <code>A</code> of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by <code>K</code>.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[4,5,0,-2,-3,1]</span>, K = <span id="example-input-1-2">5</span>
<strong>Output: </strong><span id="example-output-1">7</span>
<strong>Explanation: </strong>There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 30000</code></li>
	<li><code>-10000 &lt;= A[i] &lt;= 10000</code></li>
	<li><code>2 &lt;= K &lt;= 10000</code></li>
</ol>
</div>

-----------


## Similar Problems

- [Medium] [Subarray Sum Equals K](subarray-sum-equals-k)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Prefix Sums and Counting

**Intuition**

As is typical with problems involving subarrays, we use prefix sums to add each subarray.  Let `P[i+1] = A[0] + A[1] + ... + A[i]`.  Then, each subarray can be written as `P[j] - P[i]` (for `j > i`).  Thus, we have `P[j] - P[i]` equal to `0` modulo `K`, or equivalently `P[i]` and `P[j]` are the same value modulo `K`.

**Algorithm**

Count all the `P[i]`'s modulo `K`.  Let's say there are $$C_x$$ values $$P[i] \equiv x \pmod{K}$$.  Then, there are $$\sum_x \binom{C_x}{2}$$ possible subarrays.

For example, take `A = [4,5,0,-2,-3,1]` and `K = 5`.  Then `P = [0,4,9,9,7,4,5]`, and $$C_0 = 2, C_2 = 1, C_4 = 4$$:

* With $$C_0 = 2$$ (at $$P[0]$$, $$P[6]$$), it indicates $$\binom{2}{2} = 1$$ subarray with sum divisible by $$K$$, namely $$A[0:6] = [4, 5, 0, -2, -3, 1]$$.
* With $$C_4 = 4$$ (at $$P[1]$$, $$P[2]$$, $$P[3]$$, $$P[5]$$), it indicates $$\binom{4}{2} = 6$$ subarrays with sum divisible by $$K$$, namely $$A[1:2]$$, $$A[1:3]$$, $$A[1:5]$$, $$A[2:3]$$, $$A[2:5]$$, $$A[3:5]$$.

<iframe src="https://leetcode.com/playground/oRReLTA2/shared" frameBorder="0" width="100%" height="344" name="oRReLTA2"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.  (However, the solution can be modified to use $$O(K)$$ space by storing only `count`.)
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
