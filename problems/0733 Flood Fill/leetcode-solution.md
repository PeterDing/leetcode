# 0733 - Flood Fill

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Easy | Depth-first Search | [Leetcode](https://leetcode.com/problems/flood-fill) | [solution](https://leetcode.com/problems/flood-fill/solution/)


-----------

<p>
An <code>image</code> is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
</p><p>
Given a coordinate <code>(sr, sc)</code> representing the starting pixel (row and column) of the flood fill, and a pixel value <code>newColor</code>, "flood fill" the image.
</p><p>
To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on.  Replace the color of all of the aforementioned pixels with the newColor.
</p><p>
At the end, return the modified image.
</p>
<p><b>Example 1:</b><br />
<pre>
<b>Input:</b> 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
<b>Output:</b> [[2,2,2],[2,2,0],[2,0,1]]
<b>Explanation:</b> 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
</pre>
</p>

<p><b>Note:</b>
<li>The length of <code>image</code> and <code>image[0]</code> will be in the range <code>[1, 50]</code>.</li>
<li>The given starting pixel will satisfy <code>0 <= sr < image.length</code> and <code>0 <= sc < image[0].length</code>.</li>
<li>The value of each color in <code>image[i][j]</code> and <code>newColor</code> will be an integer in <code>[0, 65535]</code>.</li>
</p>

-----------


## Similar Problems

- [Easy] [Island Perimeter](island-perimeter)




## Solution:

[TOC]

#### Approach #1: Depth-First Search [Accepted]

**Intuition**

We perform the algorithm explained in the problem description: paint the starting pixels, plus adjacent pixels of the same color, and so on.

**Algorithm**

Say `color` is the color of the starting pixel.  Let's floodfill the starting pixel: we change the color of that pixel to the new color, then check the 4 neighboring pixels to make sure they are valid pixels of the same `color`, and of the valid ones, we floodfill those, and so on.

We can use a function `dfs` to perform a floodfill on a target pixel.

<iframe src="https://leetcode.com/playground/iMoEAq7k/shared" frameBorder="0" width="100%" height="327" name="iMoEAq7k"></iframe>


**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the number of pixels in the image.  We might process every pixel.

* Space Complexity: $$O(N)$$, the size of the implicit call stack when calling `dfs`.

---

Analysis written by: [@awice](https://leetcode.com/awice).