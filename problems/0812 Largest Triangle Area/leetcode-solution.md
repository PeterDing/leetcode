# 0812 - Largest Triangle Area

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Math | [Leetcode](https://leetcode.com/problems/largest-triangle-area) | [solution](https://leetcode.com/problems/largest-triangle-area/solution/)


-----------

<p>You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.</p>

<pre>
<strong>Example:</strong>
<strong>Input:</strong> points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> 
The five points are show in the figure below. The red triangle is the largest.
</pre>

<p><img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png" style="height:328px; width:400px" /></p>

<p><strong>Notes: </strong></p>

<ul>
	<li><code>3 &lt;= points.length &lt;= 50</code>.</li>
	<li>No points will be duplicated.</li>
	<li>&nbsp;<code>-50 &lt;= points[i][j] &lt;= 50</code>.</li>
	<li>Answers within&nbsp;<code>10^-6</code>&nbsp;of the true value will be accepted as correct.</li>
</ul>

<p>&nbsp;</p>


-----------


## Similar Problems

- [Easy] [Largest Perimeter Triangle](largest-perimeter-triangle)




## Solution:

[TOC]

---
#### Approach #1: Brute Force [Accepted]

**Intuition**

For each possible triangle, check it's area and keep the area of the largest.

**Algorithm**

We will have 3 for loops to cycle through each choice of 3 points in the array.

After, we'll need a function to calculate the area given 3 points.  Here we have some options:

* We can use the Shoelace formula directly, which tells us the area given the 3 points;

* We can use Heron's formula, which requires the 3 side lengths which we can get by taking the distance of two points;

* We can use the formula `area = 0.5 * a * b * sin(C)` and calculate the angle `C` with trigonometry.

Our implementation illustrates the use of the shoelace formula.

If we did not know the shoelace formula, we could derive it for triangles with the following approach: starting with points `(px, py), (qx, qy), (rx, ry)`, the area of this triangle is the same under a translation by `(-rx, -ry)`, so that the points become `(px-rx, py-ry), (qx-rx, qy-ry), (0, 0)`.

From there, we could draw a square around the triangle with sides touching the coordinate axes, and calculate the area of the square minus the area of the right triangles surrounding the inner triangle.

For more on this approach, see the [Wikipedia entry for the Shoelace formula](https://en.wikipedia.org/wiki/Shoelace_formula).

<iframe src="https://leetcode.com/playground/n9XwHjZg/shared" frameBorder="0" width="100%" height="327" name="n9XwHjZg"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^3)$$, where $$N$$ is the length of `points`.  We use three for-loops of length $$O(N)$$, and our work calculating the area of a single triangle is $$O(1)$$.

* Space Complexity: $$O(1)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
