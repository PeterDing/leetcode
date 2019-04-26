# 0661 - Image Smoother

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Array | [Leetcode](https://leetcode.com/problems/image-smoother) | [solution](https://leetcode.com/problems/image-smoother/solution/)


-----------

<p>Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself.  If a cell has less than 8 surrounding cells, then use as many as you can.</p>

<p><b>Example 1:</b><br />
<pre>
<b>Input:</b>
[[1,1,1],
 [1,0,1],
 [1,1,1]]
<b>Output:</b>
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
<b>Explanation:</b>
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
</pre>
</p>

<p><b>Note:</b><br>
<ol>
<li>The value in the given matrix is in the range of [0, 255].</li>
<li>The length and width of the given matrix are in the range of [1, 150].</li>
</ol>
</p>

-----------


## Similar Problems




## Solution:

[TOC]

---
#### Approach #1: Iterate Through Grid

**Intuition and Algorithm**

For each cell in the grid, look at the immediate neighbors - up to 9 of them, including the original cell.

Then, we will add the sum of the neighbors into `ans[r][c]` while recording `count`, the number of such neighbors.  The final answer is the sum divided by the count.

<iframe src="https://leetcode.com/playground/i8A5ppzu/shared" frameBorder="0" width="100%" height="395" name="i8A5ppzu"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the number of pixels in our image.  We iterate over every pixel.

* Space Complexity: $$O(N)$$, the size of our answer.

---

Analysis written by: [@awice](https://leetcode.com/awice).
