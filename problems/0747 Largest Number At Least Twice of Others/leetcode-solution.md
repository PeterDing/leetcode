# 0747 - Largest Number At Least Twice of Others

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/largest-number-at-least-twice-of-others) | [solution](https://leetcode.com/problems/largest-number-at-least-twice-of-others/solution/)


-----------

<p>In a given integer array <code>nums</code>, there is always exactly one largest element.</p>

<p>Find whether the largest element in the array is at least twice as much as every other number in the array.</p>

<p>If it is, return the <strong>index</strong> of the largest element, otherwise return -1.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3, 6, 1, 0]
<strong>Output:</strong> 1
<strong>Explanation:</strong> 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
</pre>

<p>&nbsp;</p>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1, 2, 3, 4]
<strong>Output:</strong> -1
<strong>Explanation:</strong> 4 isn&#39;t at least as big as twice the value of 3, so we return -1.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>nums</code> will have a length in the range <code>[1, 50]</code>.</li>
	<li>Every <code>nums[i]</code> will be an integer in the range <code>[0, 99]</code>.</li>
</ol>

<p>&nbsp;</p>


-----------


## Similar Problems




## Solution:

[TOC]

#### Approach #1: Linear Scan [Accepted]

**Intuition and Algorithm**

Scan through the array to find the unique largest element `m`, keeping track of it's index `maxIndex`.

Scan through the array again.  If we find some `x != m` with `m < 2*x`, we should return `-1`.

Otherwise, we should return `maxIndex`.

<iframe src="https://leetcode.com/playground/j3xuZ4yh/shared" frameBorder="0" width="100%" height="293" name="j3xuZ4yh"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$ where $$N$$ is the length of `nums`.

* Space Complexity: $$O(1)$$, the space used by our `int` variables.

---

Analysis written by: [@awice](https://leetcode.com/awice).
