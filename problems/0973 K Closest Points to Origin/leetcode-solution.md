# 0973 - K Closest Points to Origin

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Divide and Conquer, Heap, Sort | [Leetcode](https://leetcode.com/problems/k-closest-points-to-origin) | [solution](https://leetcode.com/problems/k-closest-points-to-origin/solution/)


-----------

<p>We have a list of <code>points</code>&nbsp;on the plane.&nbsp; Find the <code>K</code> closest points to the origin <code>(0, 0)</code>.</p>

<p>(Here, the distance between two points on a plane is the Euclidean distance.)</p>

<p>You may return the answer in any order.&nbsp; The&nbsp;answer is guaranteed to be unique (except for the order that it is in.)</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>points = <span id="example-input-1-1">[[1,3],[-2,2]]</span>, K = <span id="example-input-1-2">1</span>
<strong>Output: </strong><span id="example-output-1">[[-2,2]]</span>
<strong>Explanation: </strong>
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) &lt; sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>points = <span id="example-input-2-1">[[3,3],[5,-1],[-2,4]]</span>, K = <span id="example-input-2-2">2</span>
<strong>Output: </strong><span id="example-output-2">[[3,3],[-2,4]]</span>
(The answer [[-2,4],[3,3]] would also be accepted.)
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= K &lt;= points.length &lt;= 10000</code></li>
	<li><code>-10000 &lt; points[i][0] &lt; 10000</code></li>
	<li><code>-10000 &lt; points[i][1] &lt; 10000</code></li>
</ol>
</div>
</div>

-----------


## Similar Problems

- [Medium] [Kth Largest Element in an Array](kth-largest-element-in-an-array)

- [Medium] [Top K Frequent Elements](top-k-frequent-elements)

- [Medium] [Top K Frequent Words](top-k-frequent-words)




## Solution:

[TOC]

## Solution
---
#### Approach 1: Sort

**Intuition**

Sort the points by distance, then take the closest K points.

**Algorithm**

There are two variants.

In Java, we find the K-th distance by creating an array of distances and then sorting them.  After, we select all the points with distance less than or equal to this K-th distance.

In Python, we sort by a custom key function - namely, the distance to the origin.  Afterwards, we return the first K elements of the list.

<iframe src="https://leetcode.com/playground/qsCBvg6X/shared" frameBorder="0" width="100%" height="429" name="qsCBvg6X"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `points`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Divide and Conquer

**Intuition**

We want an algorithm faster than $$N \log N$$.  Clearly, the only way to do this is to use the fact that the K elements returned can be in any order -- otherwise we would be sorting which is at least $$N \log N$$.

Say we choose some random element `x = A[i]` and split the array into two buckets: one bucket of all the elements less than `x`, and another bucket of all the elements greater than or equal to `x`.  This is known as "quickselecting by a pivot `x`".

The idea is that if we quickselect by some pivot, on average in linear time we'll reduce the problem to a problem of half the size.

**Algorithm**

Let's do the `work(i, j, K)` of partially sorting the subarray `(points[i], points[i+1], ..., points[j])` so that the smallest `K` elements of this subarray occur in the first `K` positions `(i, i+1, ..., i+K-1)`.

First, we quickselect by a random pivot element from the subarray.  To do this in place, we have two pointers `i` and `j`, and move these pointers to the elements that are in the wrong bucket -- then, we swap these elements.

After, we have two buckets `[oi, i]` and `[i+1, oj]`, where `(oi, oj)` are the original `(i, j)` values when calling `work(i, j, K)`.  Say the first bucket has `10` items and the second bucket has `15` items.  If we were trying to partially sort say, `K = 5` items, then we only need to partially sort the first bucket: `work(oi, i, 5)`.  Otherwise, if we were trying to partially sort say, `K = 17` items, then the first `10` items are already partially sorted, and we only need to partially sort the next 7 items: `work(i+1, oj, 7)`.

<iframe src="https://leetcode.com/playground/9yZ96Kwf/shared" frameBorder="0" width="100%" height="500" name="9yZ96Kwf"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$ in *average case* complexity, where $$N$$ is the length of `points`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
