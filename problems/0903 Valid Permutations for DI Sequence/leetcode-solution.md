# 0903 - Valid Permutations for DI Sequence

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Divide and Conquer, Dynamic Programming | [Leetcode](https://leetcode.com/problems/valid-permutations-for-di-sequence) | [solution](https://leetcode.com/problems/valid-permutations-for-di-sequence/solution/)


-----------

<p>We are given <code>S</code>, a length <code>n</code> string of characters from the set <code>{&#39;D&#39;, &#39;I&#39;}</code>. (These letters stand for &quot;decreasing&quot; and &quot;increasing&quot;.)</p>

<p>A&nbsp;<em>valid permutation</em>&nbsp;is a permutation <code>P[0], P[1], ..., P[n]</code> of integers&nbsp;<code>{0, 1, ..., n}</code>, such that for all <code>i</code>:</p>

<ul>
	<li>If <code>S[i] == &#39;D&#39;</code>, then <code>P[i] &gt; P[i+1]</code>, and;</li>
	<li>If <code>S[i] == &#39;I&#39;</code>, then <code>P[i] &lt; P[i+1]</code>.</li>
</ul>

<p>How many valid permutations are there?&nbsp; Since the answer may be large, <strong>return your answer modulo <code>10^9 + 7</code></strong>.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">&quot;DID&quot;</span>
<strong>Output: </strong><span id="example-output-1">5</span>
<strong>Explanation: </strong>
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= S.length &lt;= 200</code></li>
	<li><code>S</code> consists only of characters from the set <code>{&#39;D&#39;, &#39;I&#39;}</code>.</li>
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
#### Approach 1: Dynamic Programming

**Intuition**

When writing the permutation `P = P_0, P_1, ..., P_N` from left to right, we only care about the relative rank of the last element placed.  For example, if `N = 5` (so that we have elements `{0, 1, 2, 3, 4, 5}`), and our permutation starts `2, 3, 4`, then it is similar to a situation where we have placed `?, ?, 2` and the remaining elements are `{0, 1, 3}`, in terms of how many possibilities there are to place the remaining elements in a valid way.

To this end, let `dp(i, j)` be the number of ways to place every number up to and inlcuding `P_i`, such that `P_i` when placed had relative rank `j`.  (Namely, there are `j` remaining numbers less than `P_i`.)

**Algorithm**

When placing `P_i` following a decreasing instruction `S[i-1] == 'D'`, we want `P_{i-1}` to have a higher value.  When placing `P_i` following an increasing instruction, we want `P_{i-1}` to have a lower value.  It is relatively easy to deduce the recursion from this fact.

<iframe src="https://leetcode.com/playground/ymMfbxds/shared" frameBorder="0" width="100%" height="500" name="ymMfbxds"></iframe>


**Optimization**

Actually, we can do better than this.  For any given `i`, let's look at how the sum of `D_k = dp(i-1, k)` is queried.  Assuming `S[i-1] == 'I'`, we query `D_0, D_0 + D_1, D_0 + D_1 + D_2, ...` etc.  The case for `S[i-1] == 'D'` is similar.

Thus, we don't need to query the sum every time.  Instead, we could use (for `S[i-1] == 'I'`) the fact that `dp(i, j) = dp(i, j-1) + dp(i-1, j-1)`.  For `S[i-1] == 'D'`, we have the similar fact that `dp(i, j) = dp(i, j+1) + dp(i-1, j)`.  

These two facts make the work done for each state of `dp` have $$O(1)$$ (amortized) complexity, leading to a total time complexity of $$O(N^2)$$ for this solution.

<iframe src="https://leetcode.com/playground/yKpXsoX7/shared" frameBorder="0" width="100%" height="395" name="yKpXsoX7"></iframe>


**Complexity Analysis**

* Time Complexity:  $$O(N^3)$$, where $$N$$ is the length of `S`, or $$O(N^2)$$ with the optimized version.

* Space Complexity:  $$O(N^2)$$.
<br />
<br />


---
#### Approach 2: Divide and Conquer

**Intuition**

Let's place the zero of the permutation first.  It either goes between a `'DI'` part of the sequence, or it could go on the ends (the left end if it starts with `'I'`, and the right end if it ends in `'D'`.)  Afterwards, this splits the problem into two disjoint subproblems that we can solve with similar logic.

**Algorithm**

Let `dp(i, j)` be the number of valid permutations (of `n = j-i+2` total integers from `0` to `n-1`) corresponding to the DI sequence `S[i], S[i+1], ..., S[j]`.  If we can successfully place a zero between `S[k-1]` and `S[k]`, then there are two disjoint problems `S[i], ..., S[k-2]` and `S[k+1], ..., S[j]`.

To count the number of valid permutations in this case, we should choose `k-i` elements from `n-1` (`n` total integers, minus the zero) to put in the left group; then the answer is this, times the number of ways to arrange the left group [`dp(i, k-2)`], times the number of ways to arrange the right group [`dp(k+1, j)`].

<iframe src="https://leetcode.com/playground/KreEbZYZ/shared" frameBorder="0" width="100%" height="500" name="KreEbZYZ"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `S`.

* Space Complexity:  $$O(N^2)$$.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).
