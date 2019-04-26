# 0798 - Smallest Rotation with Highest Score

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard |  | [Leetcode](https://leetcode.com/problems/smallest-rotation-with-highest-score) | [solution](https://leetcode.com/problems/smallest-rotation-with-highest-score/solution/)


-----------

<p>&nbsp;Given an array <code>A</code>, we may rotate it by a non-negative integer <code>K</code> so that the array becomes <code>A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1]</code>.&nbsp; Afterward, any entries that are less than or equal to their index are worth 1 point.&nbsp;</p>

<p>For example, if we have <code>[2, 4, 1, 3, 0]</code>, and we rotate by <code>K = 2</code>, it becomes <code>[1, 3, 0, 2, 4]</code>.&nbsp; This is worth 3 points because 1 &gt; 0 [no points], 3 &gt; 1 [no points], 0 &lt;= 2 [one point], 2 &lt;= 3 [one point], 4 &lt;= 4 [one point].</p>

<p>Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.&nbsp; If there are multiple answers, return the smallest such index K.</p>

<pre>
<strong>Example 1:</strong>
<strong>Input:</strong> [2, 3, 1, 4, 0]
<strong>Output:</strong> 3
<strong>Explanation: </strong> 
Scores for each K are listed below: 
K = 0,  A = [2,3,1,4,0],    score 2
K = 1,  A = [3,1,4,0,2],    score 3
K = 2,  A = [1,4,0,2,3],    score 3
K = 3,  A = [4,0,2,3,1],    score 4
K = 4,  A = [0,2,3,1,4],    score 3
</pre>

<p>So we should choose K = 3, which has the highest score.</p>

<p>&nbsp;</p>

<pre>
<strong>Example 2:</strong>
<strong>Input:</strong> [1, 3, 0, 2, 4]
<strong>Output:</strong> 0
<strong>Explanation: </strong> A will always have 3 points no matter how it shifts.
So we will choose the smallest K, which is 0.
</pre>

<p><strong>Note:</strong></p>

<ul>
	<li><code>A</code>&nbsp;will have&nbsp;length at most <code>20000</code>.</li>
	<li><code>A[i]</code> will be in the range <code>[0, A.length]</code>.</li>
</ul>


-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Interval Stabbing [Accepted]

**Intuition**

Say `N = 10` and `A[2] = 5`.  Then there are 5 rotations that are bad for this number: rotation indexes `0, 1, 2, 8, 9` - these rotations will cause this number to not get 1 point later.

In general, for each number in the array, we can map out what rotation indexes will be bad for this number.  It will always be a region of one interval, possibly two if the interval wraps around (eg. `8, 9, 0, 1, 2` wraps around, to become `[8, 9]` and `[0, 1, 2]`.)

At the end of plotting these intervals, we need to know which rotation index has the least intervals overlapping it - this one is the answer.

**Algorithm**

First, an element like `A[2] = 5` will not get score in (up to) 5 posiitons: when the 5 is at final index 0, 1, 2, 3, or 4.  When we shift by 2, we'll get final index 0.  If we shift `5-1 = 4` before this, this element will end up at final index 4.  In general (modulo N), a shift of `i - A[i] + 1` to `i` will be the rotation indexes that will make `A[i]` not score a point.

If we are trying to plot an interval like `[2, 3, 4]`, then instead of doing `bad[2]--; bad[3]--; bad[4]--;`, what we will do instead is keep track of the cumulative total: `bad[2]--; bad[5]++`.  For "wrap-around" intervals like `[8, 9, 0, 1, 2]`, we will keep track of this as two separate intervals: `bad[8]--, bad[10]++, bad[0]--, bad[3]++`.  (Actually, because of our implementation, we don't need to remember the `bad[10]++` part.)

At the end, we want to find a rotation index with the least intervals overlapping.  We'll maintain a cumulative total `cur` representing how many intervals are currently overlapping our current rotation index, then update it as we step through each rotation index.

<iframe src="https://leetcode.com/playground/wYbwGZmT/shared" frameBorder="0" width="100%" height="480" name="wYbwGZmT"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity: $$O(N)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
