# 0054 - Spiral Matrix

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Array | [Leetcode](https://leetcode.com/problems/spiral-matrix) | [solution](https://leetcode.com/problems/spiral-matrix/solution/)


-----------

<p>Given a matrix of <em>m</em> x <em>n</em> elements (<em>m</em> rows, <em>n</em> columns), return all elements of the matrix in spiral order.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong>
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
<strong>Output:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<p><strong>Example 2:</strong></p>
<pre>
<strong>Input:</strong>
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
<strong>Output:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>

-----------


## Similar Problems

- [Medium] [Spiral Matrix II](spiral-matrix-ii)




## Solution:

[TOC]

#### Approach 1: Simulation

**Intuition**

Draw the path that the spiral makes.  We know that the path should turn clockwise whenever it would go out of bounds or into a cell that was previously visited.

**Algorithm**

Let the array have $$\text{R}$$ rows and $$\text{C}$$ columns.  $$\text{seen[r][c]}$$ denotes that the cell on the$$\text{r}$$-th row and $$\text{c}$$-th column was previously visited.  Our current position is $$\text{(r, c)}$$, facing direction $$\text{di}$$, and we want to visit $$\text{R}$$ x $$\text{C}$$ total cells.

As we move through the matrix, our candidate next position is $$\text{(cr, cc)}$$.  If the candidate is in the bounds of the matrix and unseen, then it becomes our next position; otherwise, our next position is the one after performing a clockwise turn.


<iframe src="https://leetcode.com/playground/62u9UXjz/shared" frameBorder="0" width="100%" height="497" name="62u9UXjz"></iframe>


**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the total number of elements in the input matrix.  We add every element in the matrix to our final answer.

* Space Complexity: $$O(N)$$, the information stored in `seen` and in `ans`.
<br />
<br />
---
#### Approach 2: Layer-by-Layer

**Intuition**

The answer will be all the elements in clockwise order from the first-outer layer, followed by the elements from the second-outer layer, and so on.

**Algorithm**

We define the $$\text{k}$$-th outer layer of a matrix as all elements that have minimum distance to some border equal to $$\text{k}$$.  For example, the following matrix has all elements in the first-outer layer equal to 1, all elements in the second-outer layer equal to 2, and all elements in the third-outer layer equal to 3.

```plain-text
[[1, 1, 1, 1, 1, 1, 1],
 [1, 2, 2, 2, 2, 2, 1],
 [1, 2, 3, 3, 3, 2, 1],
 [1, 2, 2, 2, 2, 2, 1],
 [1, 1, 1, 1, 1, 1, 1]]
```

For each outer layer, we want to iterate through its elements in clockwise order starting from the top left corner.  Suppose the current outer layer has top-left coordinates $$\text{(r1, c1)}$$ and bottom-right coordinates $$\text{(r2, c2)}$$.

Then, the top row is the set of elements $$\text{(r1, c)}$$ for $$\text{c = c1,...,c2}$$, in that order.  The rest of the right side is the set of elements $$\text{(r, c2)}$$ for $$\text{r = r1+1,...,r2}$$, in that order.  Then, if there are four sides to this layer (ie., $$\text{r1 < r2}$$ and $$\text{c1 < c2}$$), we iterate through the bottom side and left side as shown in the solutions below.

![SpiralMatrix](../Figures/54_spiralmatrix.png)

<iframe src="https://leetcode.com/playground/hWE2c3x4/shared" frameBorder="0" width="100%" height="446" name="hWE2c3x4"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the total number of elements in the input matrix.  We add every element in the matrix to our final answer.

* Space Complexity: $$O(N)$$, the information stored in `ans`.
