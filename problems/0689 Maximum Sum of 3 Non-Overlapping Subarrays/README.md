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




## Thought:
