# 0015 - 3Sum

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array, Two Pointers | [Leetcode](https://leetcode.com/problems/3sum) | [solution](https://leetcode.com/problems/3sum/solution/)

-----------

<p>Given an array <code>nums</code> of <em>n</em> integers, are there elements <em>a</em>, <em>b</em>, <em>c</em> in <code>nums</code> such that <em>a</em> + <em>b</em> + <em>c</em> = 0? Find all unique triplets in the array which gives the sum of zero.</p>

<p><strong>Note:</strong></p>

<p>The solution set must not contain duplicate triplets.</p>

<p><strong>Example:</strong></p>

<pre>
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
</pre>
-----------


## Similar Problems

- [Easy] [Two Sum](two-sum)

- [Medium] [3Sum Closest](3sum-closest)

- [Medium] [4Sum](4sum)

- [Medium] [3Sum Smaller](3sum-smaller)



## Thought:

This problem has its general version, target is T.

1. Sort the array O(nlogn)

2. Find T/3 as the pointer as A by binary search O(logn)

3. Iterate O(n) = O(2n)

   1. Select [A] point and use 2sum at [A+1 … n], then select [A-1]
   2. Select [A] point and use 2sum at [0 … A-1], then select [A+1]

So, the total O is O(nlogn + logn + n) < O(n^3)

