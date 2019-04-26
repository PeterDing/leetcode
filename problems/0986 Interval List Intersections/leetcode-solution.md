# 0986 - Interval List Intersections

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Two Pointers | [Leetcode](https://leetcode.com/problems/interval-list-intersections) | [solution](https://leetcode.com/problems/interval-list-intersections/solution/)


-----------

<p>Given two lists&nbsp;of <strong>closed</strong> intervals, each list of intervals is pairwise disjoint and in sorted order.</p>

<p>Return the intersection of these two interval lists.</p>

<p><em>(Formally, a closed interval <code>[a, b]</code> (with <code>a &lt;= b</code>) denotes&nbsp;the set of real numbers <code>x</code> with <code>a &lt;= x &lt;= b</code>.&nbsp; The&nbsp;intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.&nbsp; For example, the intersection of [1, 3] and [2, 4] is [2, 3].)</em></p>

<div>
<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2019/01/30/interval1.png" style="width: 506px; height: 140px;" /></strong></p>

<pre>
<strong>Input: </strong>A = <span id="example-input-1-1">[[0,2],[5,10],[13,23],[24,25]]</span>, B = <span id="example-input-1-2">[[1,5],[8,12],[15,24],[25,26]]</span>
<strong>Output: </strong><span id="example-output-1">[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]</span>
<strong>Reminder: </strong>The inputs and the desired output are lists of Interval&nbsp;objects, and not arrays or lists.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>0 &lt;= A.length &lt; 1000</code></li>
	<li><code>0 &lt;= B.length &lt; 1000</code></li>
	<li><code>0 &lt;= A[i].start, A[i].end, B[i].start, B[i].end &lt; 10^9</code></li>
</ol>

<p><strong>NOTE:</strong>&nbsp;input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.</p>
</div>


-----------


## Similar Problems

- [Medium] [Merge Intervals](merge-intervals)

- [Easy] [Merge Sorted Array](merge-sorted-array)

- [Hard] [Employee Free Time](employee-free-time)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Merge Intervals

**Intuition**

In an interval `[a, b]`, call `b` the "endpoint".

Among the given intervals, consider the interval `A[0]` with the smallest endpoint.  (Without loss of generality, this interval occurs in array `A`.)

Then, among the intervals in array `B`, `A[0]` can only intersect one such interval in array `B`.  (If two intervals in `B` intersect `A[0]`, then they both share the endpoint of `A[0]` -- but intervals in `B` are disjoint, which is a contradiction.)

**Algorithm**

If `A[0]` has the smallest endpoint, it can only intersect `B[0]`.  After, we can discard `A[0]` since it cannot intersect anything else.

Similarly, if `B[0]` has the smallest endpoint, it can only intersect `A[0]`, and we can discard `B[0]` after since it cannot intersect anything else.

We use two pointers, `i` and `j`, to virtually manage "discarding" `A[0]` or `B[0]` repeatedly.

<iframe src="https://leetcode.com/playground/ZoFMccAy/shared" frameBorder="0" width="100%" height="463" name="ZoFMccAy"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(M + N)$$, where $$M, N$$ are the lengths of `A` and `B` respectively.

* Space Complexity:  $$O(M + N)$$, the maximum size of the answer.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
