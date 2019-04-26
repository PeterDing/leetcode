# 0909 - Snakes and Ladders

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Breadth-first Search | [Leetcode](https://leetcode.com/problems/snakes-and-ladders) | [solution](https://leetcode.com/problems/snakes-and-ladders/solution/)


-----------

<p>On an N x N <code>board</code>, the numbers from <code>1</code> to <code>N*N</code> are written&nbsp;<em>boustrophedonically</em>&nbsp;<strong>starting from the bottom&nbsp;left of the board</strong>, and alternating direction each row.&nbsp; For example, for a 6 x 6 board, the numbers are written as follows:</p>

<pre>
<img alt="" src="https://assets.leetcode.com/uploads/2018/09/23/snakes.png" style="width: 254px; height: 200px;" />
</pre>

<p>You start on square <code>1</code> of the board (which is always in the last row and&nbsp;first column).&nbsp; Each move, starting from square <code>x</code>, consists of the following:</p>

<ul>
	<li>You choose a destination square <code>S</code> with number&nbsp;<code>x+1</code>, <code>x+2</code>, <code>x+3</code>, <code>x+4</code>, <code>x+5</code>, or <code>x+6</code>, provided this&nbsp;number is&nbsp;<code>&lt;=&nbsp;N*N</code>.

	<ul>
		<li>(This choice simulates the result of a standard 6-sided die roll: ie., there are always <strong>at most 6 destinations, regardless of the size of the board</strong>.)</li>
	</ul>
	</li>
	<li>If <code>S</code>&nbsp;has a snake or ladder, you move to the destination of that snake or ladder.&nbsp; Otherwise, you move to <code>S</code>.</li>
</ul>

<p>A board square on row <code>r</code> and column <code>c</code>&nbsp;has a &quot;snake or ladder&quot; if <code>board[r][c] != -1</code>.&nbsp; The destination of that snake or ladder is <code>board[r][c]</code>.</p>

<p>Note that you only take a snake or ladder at most once per move: if the destination to a snake or ladder is the start of another&nbsp;snake or ladder, you do <strong>not</strong> continue moving.&nbsp; (For example, if the board is `[[4,-1],[-1,3]]`, and on the first move your destination square is `2`, then you finish your first move at&nbsp;`3`, because you do <strong>not</strong> continue moving to `4`.)</p>

<p>Return the least number of moves required to reach square <font face="monospace">N*N</font>.&nbsp; If it is not possible, return <code>-1</code>.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>[
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]
<strong>Output: </strong>4
<strong>Explanation: </strong>
At the beginning, you start at square 1 [at row 5, column 0].
You decide to move to square 2, and must take the ladder to square 15.
You then decide to move to square 17 (row 3, column 5), and must take the snake to square 13.
You then decide to move to square 14, and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
It can be shown that you need at least 4 moves to reach the N*N-th square, so the answer is 4.
</pre>

<p><strong>Note:</strong></p>

<ol>
	<li><code>2 &lt;= board.length = board[0].length&nbsp;&lt;= 20</code></li>
	<li><code>board[i][j]</code>&nbsp;is between <code>1</code> and <code>N*N</code> or is equal to <code>-1</code>.</li>
	<li>The board&nbsp;square with number <code>1</code> has no snake or ladder.</li>
	<li>The board square with number <code>N*N</code> has no snake or ladder.</li>
</ol>


-----------


## Similar Problems




## Solution:

[TOC]

## Solution
---
#### Approach 1: Breadth-First Search

**Intuition**

As we are looking for a shortest path, a breadth-first search is ideal.  The main difficulty is to handle enumerating all possible moves from each square.

**Algorithm**

Suppose we are on a square with number `s`.  We would like to know all final destinations with number `s2` after making one move.

This requires knowing the coordinates `get(s2)` of square `s2`.  This is a small puzzle in itself: we know that the row changes every `N` squares, and so is only based on `quot = (s2-1) / N`; also the column is only based on `rem = (s2-1) % N` and what row we are on (forwards or backwards.)

From there, we perform a breadth first search, where the nodes are the square numbers `s`.

<iframe src="https://leetcode.com/playground/RZ7eqY32/shared" frameBorder="0" width="100%" height="500" name="RZ7eqY32"></iframe>

**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the length of the `board`.

* Space Complexity:  $$O(N^2)$$.
<br />
<br />


---

Analysis written by: [@awice](https://leetcode.com/awice).
