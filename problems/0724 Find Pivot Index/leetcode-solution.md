# 0724 - Find Pivot Index

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/find-pivot-index) | [solution](https://leetcode.com/problems/find-pivot-index/solution/)


-----------

<p>Given an array of integers <code>nums</code>, write a method that returns the &quot;pivot&quot; index of this array.</p>

<p>We define the pivot index as the index where the sum of the numbers to the left of the index is equal to the sum of the numbers to the right of the index.</p>

<p>If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> 
nums = [1, 7, 3, 6, 5, 6]
<b>Output:</b> 3
<b>Explanation:</b> 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
</pre>

<p>&nbsp;</p>

<p><b>Example 2:</b></p>

<pre>
<b>Input:</b> 
nums = [1, 2, 3]
<b>Output:</b> -1
<b>Explanation:</b> 
There is no index that satisfies the conditions in the problem statement.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li>The length of <code>nums</code> will be in the range <code>[0, 10000]</code>.</li>
	<li>Each element <code>nums[i]</code> will be an integer in the range <code>[-1000, 1000]</code>.</li>
</ul>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Medium] [Subarray Sum Equals K](subarray-sum-equals-k)




## Solution:

[TOC]

#### Approach #1: Prefix Sum [Accepted]

**Intuition and Algorithm**

We need to quickly compute the sum of values to the left and the right of every index.

Let's say we knew `S` as the sum of the numbers, and we are at index `i`.  If we knew the sum of numbers `leftsum` that are to the left of index `i`, then the other sum to the right of the index would just be `S - nums[i] - leftsum`.  

As such, we only need to know about `leftsum` to check whether an index is a pivot index in constant time.  Let's do that: as we iterate through candidate indexes `i`, we will maintain the correct value of `leftsum`.

<iframe src="https://leetcode.com/playground/332EfbBV/shared" frameBorder="0" width="100%" height="242" name="332EfbBV"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the length of `nums`.

* Space Complexity: $$O(1)$$, the space used by `leftsum` and `S`.

---

Analysis written by: [@awice](https://leetcode.com/awice).
