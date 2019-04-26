# 0963 - Minimum Area Rectangle II

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Math, Geometry | [Leetcode](https://leetcode.com/problems/minimum-area-rectangle-ii) | [solution](https://leetcode.com/problems/minimum-area-rectangle-ii/solution/)


-----------

<p>Given a set of points in the xy-plane, determine the minimum area of <strong>any</strong> rectangle formed from these points, with sides <strong>not necessarily parallel</strong> to the x and y axes.</p>

<p>If there isn&#39;t any rectangle, return 0.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2018/12/21/1a.png" style="width: 150px; height: 151px;" /></p>

<pre>
<strong>Input: </strong><span id="example-input-1-1">[[1,2],[2,1],[1,0],[0,1]]</span>
<strong>Output: </strong><span id="example-output-1">2.00000
<strong>Explanation:</strong> </span><span>The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.</span>
</pre>

<div>
<p><strong>Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2018/12/22/2.png" style="width: 150px; height: 94px;" /></p>

<pre>
<strong>Input: </strong><span id="example-input-2-1">[[0,1],[2,1],[1,1],[1,0],[2,0]]</span>
<strong>Output: </strong><span id="example-output-2">1.00000
</span><strong>Explanation:</strong> The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
</pre>

<div>
<p><strong>Example 3:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2018/12/22/3.png" style="width: 160px; height: 167px;" /></p>

<pre>
<strong>Input: </strong><span id="example-input-3-1">[[0,3],[1,2],[3,1],[1,3],[2,1]]</span>
<strong>Output: </strong><span id="example-output-3">0
</span><span><strong>Explanation:</strong> There is no possible rectangle to form from these points.</span>
</pre>

<div>
<p><strong>Example 4:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2018/12/21/4c.png" style="width: 160px; height: 155px;" /></p>

<pre>
<strong>Input: </strong><span id="example-input-4-1">[[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]</span>
<strong>Output: </strong><span id="example-output-4">2.00000
</span><span><strong>Explanation:</strong> The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.</span>
</pre>
</div>

<p>&nbsp;</p>
</div>
</div>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= points.length &lt;= 50</code></li>
	<li><code>0 &lt;=&nbsp;points[i][0] &lt;=&nbsp;40000</code></li>
	<li><code>0 &lt;=&nbsp;points[i][1] &lt;=&nbsp;40000</code></li>
	<li>All points are distinct.</li>
	<li>Answers within <code>10^-5</code> of the actual value will be accepted as correct.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Iterate Triangles

**Intuition**

For each triangle, let's try to find the 4th point and whether it is a rectangle.

**Algorithm**

Say the first 3 points are `p1, p2, p3`, and that  `p2` and `p3` are opposite corners of the final rectangle.  The 4th point must be `p4 = p2 + p3 - p1` (using vector notation) because `p1, p2, p4, p3` must form a parallelogram, and `p1 + (p2 - p1) + (p3 - p1) = p4`.

If this point exists in our collection (we can use a `HashSet` to check), then we should check that the angles of this parallelogram are 90 degrees.  The easiest way is to check the dot product of the two vectors `(p2 - p1)` and `(p3 - p1)`.  (Another way is we could normalize the vectors to length 1, and check that one equals the other rotated by 90 degrees.)

<iframe src="https://leetcode.com/playground/4L9BqZN7/shared" frameBorder="0" width="100%" height="500" name="4L9BqZN7"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^3)$$, where $$N$$ is the length of `points`.

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
#### Approach 2: Iterate Centers

**Intuition**

Consider opposite points `AC` and `BD` of a rectangle `ABCD`.  They both have the same center `O`, which is the midpoint of `AC` and the midpoint of `AB`; and they both have the same radius `dist(O, A) == dist(O, B) == dist(O, C) == dist(O, D)`.  Notice that a necessary and sufficient condition to form a rectangle with two opposite pairs of points is that the points must have the same center and radius.

Motivated by that result, let's classify each pair of points `PQ` by their center `C` = the midpoint of `PQ`, and the radius `r = dist(P, C)`.  Our strategy is to brute force on pairs of points with the same classification.

**Algorithm**

For each pair of points, classify them by `center` and `radius`.  We only need to record one of the points `P`, since the other point is `P' = 2 * center - P` (using vector notation).

For each `center` and `radius`, look at every possible rectangle (two pairs of points `P, P', Q, Q'`).  The area of this rectangle `dist(P, Q) * dist(P, Q')` is a candidate answer.

<iframe src="https://leetcode.com/playground/2wzCpbAU/shared" frameBorder="0" width="100%" height="500" name="2wzCpbAU"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2 \log N)$$, where $$N$$ is the length of `points`.  It can be shown that the number of pairs of points with the same classification is bounded by $$\log N$$ - [see this link for more.](https://en.wikipedia.org/wiki/Sum_of_squares_function#Particular_cases)

* Space Complexity:  $$O(N)$$.
<br />
<br />


---
Analysis written by: [@awice](https://leetcode.com/awice).
