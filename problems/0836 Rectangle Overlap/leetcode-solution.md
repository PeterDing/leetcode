# 0836 - Rectangle Overlap

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Math | [Leetcode](https://leetcode.com/problems/rectangle-overlap) | [solution](https://leetcode.com/problems/rectangle-overlap/solution/)


-----------

<p>A rectangle is&nbsp;represented as a&nbsp;list <code>[x1, y1, x2, y2]</code>, where&nbsp;<code>(x1, y1)</code>&nbsp;are the coordinates of its bottom-left corner, and <code>(x2,&nbsp;y2)</code>&nbsp;are the coordinates of its top-right corner.</p>

<p>Two rectangles overlap if the area of their intersection is positive.&nbsp; To be clear, two rectangles that only touch at the corner or edges do not overlap.</p>

<p>Given two (axis-aligned) rectangles, return whether&nbsp;they overlap.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>rec1 = [0,0,2,2], rec2 = [1,1,3,3]
<strong>Output: </strong>true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input: </strong>rec1 = [0,0,1,1], rec2 = [1,0,2,1]
<strong>Output: </strong>false
</pre>

<p><strong>Notes:</strong></p>

<ol>
	<li>Both rectangles <code>rec1</code> and <code>rec2</code> are lists of 4 integers.</li>
	<li>All coordinates in rectangles will be between&nbsp;<code>-10^9 </code>and<code> 10^9</code>.</li>
</ol>


-----------


## Similar Problems

- [Medium] [Rectangle Area](rectangle-area)




## Solution:

[TOC]

#### Approach #1: Check Position [Accepted]

**Intuition**

If the rectangles do not overlap, then `rec1` must either be higher, lower, to the left, or to the right of `rec2`.

**Algorithm**

The answer for whether they *don't* overlap is `LEFT OR RIGHT OR UP OR DOWN`, where `OR` is the logical OR, and `LEFT` is a boolean that represents whether `rec1` is to the left of `rec2`.  The answer for whether they do overlap is the negation of this.

The condition "`rec1` is to the left of `rec2`" is `rec1[2] <= rec2[0]`, that is the right-most x-coordinate of `rec1` is left of the left-most x-coordinate of `rec2`.  The other cases are similar.

<iframe src="https://leetcode.com/playground/XsHWyYAa/shared" frameBorder="0" width="100%" height="191" name="XsHWyYAa"></iframe>

**Complexity Analysis**

* Time and Space Complexity:  $$O(1)$$.

---
#### Approach #2: Check Area [Accepted]

**Intuition**

If the rectangles overlap, they have positive area.  This area must be a rectangle where both dimensions are positive, since the boundaries of the intersection are axis aligned.

Thus, we can reduce the problem to the one-dimensional problem of determining whether two line segments overlap.

**Algorithm**

Say the area of the intersection is `width * height`, where `width` is the intersection of the rectangles projected onto the x-axis, and `height` is the same for the y-axis.  We want both quantities to be positive.

The `width` is positive when `min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])`, that is when the smaller of (the largest x-coordinates) is larger than the larger of (the smallest x-coordinates).  The `height` is similar.

<iframe src="https://leetcode.com/playground/gthZq8DL/shared" frameBorder="0" width="100%" height="157" name="gthZq8DL"></iframe>

**Complexity Analysis**

* Time and Space Complexity:  $$O(1)$$.

---

Analysis written by: [@awice](https://leetcode.com/awice).
