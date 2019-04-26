# 0689 - Maximum Sum of 3 Non-Overlapping Subarrays

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Array, Dynamic Programming | [Leetcode](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays) | [solution](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/solution/)


-----------

<p>
In a given array <code>nums</code> of positive integers, find three non-overlapping subarrays with maximum sum.
</p>
<p>
Each subarray will be of size <code>k</code>, and we want to maximize the sum of all <code>3*k</code> entries.
</p>
<p>
Return the result as a list of indices representing the starting position of each interval (0-indexed).  If there are multiple answers, return the lexicographically smallest one.
</p>
<p><b>Example:</b><br />
<pre>
<b>Input:</b> [1,2,1,2,6,7,5,1], 2
<b>Output:</b> [0, 3, 5]
<b>Explanation:</b> Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
</pre>
</p>

<p><b>Note:</b><br />
<li><code>nums.length</code> will be between 1 and 20000.</li>
<li><code>nums[i]</code> will be between 1 and 65535.</li>
<li><code>k</code> will be between 1 and floor(nums.length / 3).</li>
</p>

-----------


## Similar Problems

- [Hard] [Best Time to Buy and Sell Stock III](best-time-to-buy-and-sell-stock-iii)




## Solution:

[TOC]

#### Approach #1: Ad-Hoc [Accepted]

**Intuition**

It is natural to consider an array `W` of each interval's sum, where each interval is the given length `K`.  To create `W`, we can either use prefix sums, or manage the sum of the interval as a window slides along the array.

From there, we approach the reduced problem: Given some array `W` and an integer `K`, what is the lexicographically smallest tuple of indices `(i, j, k)` with `i + K <= j` and `j + K <= k` that maximizes `W[i] + W[j] + W[k]`?

**Algorithm**

Suppose we fixed `j`.  We would like to know on the intervals $$i \in [0, j-K]$$ and $$k \in [j+K, \text{len}(W)-1]$$, where the largest value of $$W[i]$$ (and respectively $$W[k]$$) occurs first.  (Here, first means the smaller index.)

We can solve these problems with dynamic programming.  For example, if we know that $$i$$ is where the largest value of $$W[i]$$ occurs first on $$[0, 5]$$, then on $$[0, 6]$$ the first occurrence of the largest $$W[i]$$ must be either $$i$$ or $$6$$.  If say, $$6$$ is better, then we set `best = 6`.

At the end, `left[z]` will be the first occurrence of the largest value of `W[i]` on the interval $$i \in [0, z]$$, and `right[z]` will be the same but on the interval $$i \in [z, \text{len}(W) - 1]$$.  This means that for some choice `j`, the candidate answer must be `(left[j-K], j, right[j+K])`.  We take the candidate that produces the maximum `W[i] + W[j] + W[k]`.

<iframe src="https://leetcode.com/playground/rcX96JEv/shared" frameBorder="0" name="rcX96JEv" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of the array.  Every loop is bounded in the number of steps by $$N$$, and does $$O(1)$$ work.

* Space complexity:  $$O(N)$$.  `W`, `left`, and `right` all take $$O(N)$$ memory.

---

Analysis written by: [@awice](https://leetcode.com/awice)
