# 0688 - Knight Probability in Chessboard

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming | [Leetcode](https://leetcode.com/problems/knight-probability-in-chessboard) | [solution](https://leetcode.com/problems/knight-probability-in-chessboard/solution/)


-----------

<p>On an <code>N</code>x<code>N</code> chessboard, a knight starts at the <code>r</code>-th row and <code>c</code>-th column and attempts to make exactly <code>K</code> moves. The rows and columns are 0 indexed, so the top-left square is <code>(0, 0)</code>, and the bottom-right square is <code>(N-1, N-1)</code>.</p>

<p>A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/12/knight.png" style="width: 200px; height: 200px;" /></p>

<p>&nbsp;</p>

<p>Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.</p>

<p>The knight continues moving until it has made exactly <code>K</code> moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.</p>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
<b>Input:</b> 3, 2, 0, 0
<b>Output:</b> 0.0625
<b>Explanation:</b> There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li><code>N</code> will be between 1 and 25.</li>
	<li><code>K</code> will be between 0 and 100.</li>
	<li>The knight always initially starts on the board.</li>
</ul>


-----------


## Similar Problems

- [Medium] [Out of Boundary Paths](out-of-boundary-paths)




## Solution:

[TOC]

#### Approach #1: Dynamic Programming [Accepted]

**Intuition and Algorithm**

Let `f[r][c][steps]` be the probability of being on square `(r, c)` after `steps` steps.  Based on how a knight moves, we have the following recursion:

$$f[r][c][steps] = \sum_{dr, dc} f[r+dr][c+dc][steps-1] / 8.0$$

where the sum is taken over the eight $$(dr, dc)$$ pairs $$(2, 1),$$ $$(2, -1),$$ $$(-2, 1),$$ $$(-2, -1),$$ $$(1, 2),$$ $$(1, -2),$$ $$(-1, 2),$$ $$(-1, -2)$$.

Instead of using a three-dimensional array `f`, we will use two two-dimensional ones `dp` and `dp2`, storing the result of the two most recent layers we are working on.  `dp2` will represent `f[][][steps]`, and `dp` will represent `f[][][steps-1]`.

<iframe src="https://leetcode.com/playground/VTNPLt6H/shared" frameBorder="0" name="VTNPLt6H" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^2 K)$$ where $$N, K$$ are defined as in the problem.  We do $$O(1)$$ work on each layer `dp` of $$N^2$$ elements, and there are $$K$$ layers considered.

* Space Complexity: $$O(N^2)$$, the size of `dp` and `dp2`.

---
#### Approach #2: Matrix Exponentiation [Accepted]

**Intuition**

The recurrence expressed in *Approach #1* expressed states that transitioned to a linear combination of other states.  Any time this happens, we can represent the entire transition as a matrix of those linear combinations.  Then, the $$n$$-th power of this matrix represents the transition of $$n$$ moves, and thus we can reduce the problem to a problem of matrix exponentiation.

**Algorithm**

First, there is a lot of symmetry on the board that we can exploit.  Naively, there are $$N^2$$ possible states the knight can be in (assuming it is on the board).  Because of symmetry through the horizontal, vertical, and diagonal axes, we can assume that the knight is in the top-left quadrant of the board, and that the column number is equal to or larger than the row number.  For any square, the square that is found by reflecting about these axes to satisfy these conditions will be the *canonical index* of that square.

This will reduce the number of states from $$N^2$$ to approximately $$\frac{N^2}{8}$$, which makes the following (cubic) matrix exponentiation on this $$O(\frac{N^2}{8}) \times O(\frac{N^2}{8})$$ matrix approximately $$8^3$$ times faster.

Now, if we know that every state becomes some linear combination of states after one move, then let's write a transition matrix $$\mathcal{T}$$ of them, where the $$i$$-th row of $$\mathcal{T}$$ represents the linear combination of states that the $$i$$-th state goes to.  Then, $$\mathcal{T}^n$$ represents a transition of $$n$$ moves, for which we want the sum of the $$i$$-th row, where $$i$$ is the index of the starting square.

<iframe src="https://leetcode.com/playground/ARu5yUUd/shared" frameBorder="0" name="ARu5yUUd" width="100%" height="515"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^6 \log(K))$$ where $$N, K$$ are defined as in the problem.  There are approximately $$\frac{N^2}{8}$$ canonical states, which makes our matrix multiplication $$O(N^6)$$.  To find the $$K$$-th power of this matrix, we make $$O(\log(K))$$ matrix multiplications.

* Space Complexity: $$O(N^4)$$.  The matrix has approximately $$\frac{N^4}{64}$$ elements.

---

Analysis written by: [@awice](https://leetcode.com/awice)
