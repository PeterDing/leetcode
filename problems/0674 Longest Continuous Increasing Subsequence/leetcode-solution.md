# 0674 - Longest Continuous Increasing Subsequence

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/longest-continuous-increasing-subsequence) | [solution](https://leetcode.com/problems/longest-continuous-increasing-subsequence/solution/)


-----------

<p>
Given an unsorted array of integers, find the length of longest <code>continuous</code> increasing subsequence (subarray).
</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> [1,3,5,4,7]
<b>Output:</b> 3
<b>Explanation:</b> The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
</pre>
</p>

<p><b>Example 2:</b><br />
<pre>
<b>Input:</b> [2,2,2,2,2]
<b>Output:</b> 1
<b>Explanation:</b> The longest continuous increasing subsequence is [2], its length is 1. 
</pre>
</p>

<p><b>Note:</b>
Length of the array will not exceed 10,000.
</p>

-----------


## Similar Problems

- [Medium] [Number of Longest Increasing Subsequence](number-of-longest-increasing-subsequence)

- [Hard] [Minimum Window Subsequence](minimum-window-subsequence)




## Solution:

[TOC]


#### Approach #1: Sliding Window [Accepted]

**Intuition and Algorithm**

Every (continuous) increasing subsequence is disjoint, and the boundary of each such subsequence occurs whenever `nums[i-1] >= nums[i]`.  When it does, it marks the start of a new increasing subsequence at `nums[i]`, and we store such `i` in the variable `anchor`.

For example, if `nums = [7, 8, 9, 1, 2, 3]`, then `anchor` starts at `0` (`nums[anchor] = 7`) and gets set again to `anchor = 3` (`nums[anchor] = 1`).  Regardless of the value of `anchor`, we record a candidate answer of `i - anchor + 1`, the length of the subarray `nums[anchor], nums[anchor+1], ..., nums[i]`; and our answer gets updated appropriately.

<iframe src="https://leetcode.com/playground/AvR7oHwg/shared" frameBorder="0" width="100%" height="225" name="AvR7oHwg"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of `nums`.  We perform one loop through `nums`.

* Space Complexity: $$O(1)$$, the space used by `anchor` and `ans`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
