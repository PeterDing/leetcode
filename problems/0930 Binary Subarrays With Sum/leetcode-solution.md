# 0930 - Binary Subarrays With Sum

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Hash Table, Two Pointers | [Leetcode](https://leetcode.com/problems/binary-subarrays-with-sum) | [solution](https://leetcode.com/problems/binary-subarrays-with-sum/solution/)


-----------

<p>In an array <code>A</code> of <code>0</code>s and <code>1</code>s, how many <strong>non-empty</strong> subarrays have sum <code>S</code>?</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[1,0,1,0,1]</span>, S = <span id="example-input-1-2">2</span>
<strong>Output: </strong><span id="example-output-1">4</span>
<strong>Explanation: </strong>
The 4 subarrays are bolded below:
[<strong>1,0,1</strong>,0,1]
[<strong>1,0,1,0</strong>,1]
[1,<strong>0,1,0,1</strong>]
[1,0,<strong>1,0,1</strong>]
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>A.length &lt;= 30000</code></li>
	<li><code>0 &lt;= S &lt;= A.length</code></li>
	<li><code>A[i]</code>&nbsp;is either <code>0</code>&nbsp;or <code>1</code>.</li>
</ol>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Index of Ones

**Intuition**

Say we number the `1`s in `A`: $$(x_1, x_2, \cdots, x_n)$$ with $$A[x_i] = 1$$.

Then, if we have a subarray of sum $$S$$, it has to use the ones $$x_i, x_{i+1}, \cdots, x_{i+S-1}$$.  For each $$i$$, we can count the number of such subarrays individually.

**Algorithm**

In general, the number of such subarrays (for $$i$$) is $$(x_i - x_{i-1}) * (x_{i+S} - x_{i+S-1})$$.

For example, if $$S = 2$$, then in `A = [1,0,1,0,1,0,0,1]`, let's count the number of subarrays `[i, j]` that use the middle two `1`s.  There are 2 choices for the `i` `(i = 1, 2)` and 3 choices for the `j` `(j = 4, 5, 6)`.

The corner cases are when $$S = 0$$, $$i = 1$$, or $$i+S = n+1$$. We can handle these gracefully.

<iframe src="https://leetcode.com/playground/xeXqLmYy/shared" frameBorder="0" width="100%" height="500" name="xeXqLmYy"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Prefix Sums

**Intuition**

Let `P[i] = A[0] + A[1] + ... + A[i-1]`.  Then `P[j+1] - P[i] = A[i] + A[i+1] + ... + A[j]`, the sum of the subarray `[i, j]`.

Hence, we are looking for the number of `i < j` with `P[j] - P[i] = S`.

**Algorithm**

For each `j`, let's count the number of `i` with `P[j] = P[i] + S`.  This is analogous to counting the number of subarrays ending in `j` with sum `S`.

It comes down to counting how many `P[i] + S` we've seen before.  We can keep this count on the side to help us find the final answer.

<iframe src="https://leetcode.com/playground/nAHXHKUL/shared" frameBorder="0" width="100%" height="344" name="nAHXHKUL"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 3: Three Pointer

**Intuition**

For each `j`, let's try to count the number of `i`'s that have the subarray `[i, j]` equal to `S`.

It is easy to see these `i`'s form an interval `[i_lo, i_hi]`, and each of `i_lo`, `i_hi` are increasing with respect to `j`.  So we can use a "two pointer" style approach.

**Algorithm**

For each `j` (in increasing order), let's maintain 4 variables:

* `sum_lo` : the sum of subarray `[i_lo, j]`
* `sum_hi` : the sum of subarray `[i_hi, j]`
* `i_lo` : the smallest `i` so that `sum_lo <= S`
* `i_hi` : the largest `i` so that `sum_hi <= S`

Then, (provided that `sum_lo == S`), the number of subarrays ending in `j` is `i_hi - i_lo + 1`.

As an example, with `A = [1,0,0,1,0,1]` and `S = 2`, when `j = 5`, we want `i_lo = 1` and `i_hi = 3`.

<iframe src="https://leetcode.com/playground/7oyzRqG8/shared" frameBorder="0" width="100%" height="480" name="7oyzRqG8"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
