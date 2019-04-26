# 0939 - Minimum Area Rectangle

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Hash Table | [Leetcode](https://leetcode.com/problems/minimum-area-rectangle) | [solution](https://leetcode.com/problems/minimum-area-rectangle/solution/)


-----------

<p>Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.</p>

<p>If there isn&#39;t any rectangle, return 0.</p>

<p>&nbsp;</p>

<div>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,1],[1,3],[3,1],[3,3],[2,2]]</span>
<strong>Output: </strong><span id="example-output-1">4</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]</span>
<strong>Output: </strong><span id="example-output-2">2</span>
</pre>

<p>&nbsp;</p>

<p><strong>Note</strong>:</p>

<ol>
	<li><code>1 &lt;= points.length &lt;= 500</code></li>
	<li><code>0 &lt;=&nbsp;points[i][0] &lt;=&nbsp;40000</code></li>
	<li><code>0 &lt;=&nbsp;points[i][1] &lt;=&nbsp;40000</code></li>
	<li>All points are distinct.</li>
</ol>
</div>
</div>

-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Sort by Column

**Intuition**

Count each rectangle by right-most edge.

**Algorithm**

Group the points by `x` coordinates, so that we have columns of points.  Then, for every pair of points in a column (with coordinates `(x,y1)` and `(x,y2)`), check for the smallest rectangle with this pair of points as the rightmost edge.  We can do this by keeping memory of what pairs of points we've seen before.

<iframe src="https://leetcode.com/playground/kTVsWSQg/shared" frameBorder="0" width="100%" height="497" name="kTVsWSQg"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `points`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Count by Diagonal

**Intuition**

For each pair of points in the array, consider them to be the long diagonal of a potential rectangle.  We can check if all 4 points are there using a Set.

For example, if the points are `(1, 1)` and `(5, 5)`, we check if we also have `(1, 5)` and `(5, 1)`.  If we do, we have a candidate rectangle.

**Algorithm**

Put all the points in a set.  For each pair of points, if the associated rectangle are 4 distinct points all in the set, then take the area of this rectangle as a candidate answer.

<iframe src="https://leetcode.com/playground/x8SzczGY/shared" frameBorder="0" width="100%" height="412" name="x8SzczGY"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of `points`.

* Space Complexity:  $$O(N)$$, where $$H$$ is the height of the tree.
<br />
<br />


---


Analysis written by: [@awice](https://leetcode.com/awice).  Approach #1 inspired by: [@lee215](https://leetcode.com/lee215).
