# 0741 - Cherry Pickup

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Hard | Dynamic Programming | [Leetcode](https://leetcode.com/problems/cherry-pickup) | [solution](https://leetcode.com/problems/cherry-pickup/solution/)


-----------

<p>In a N x N <code>grid</code> representing a field of cherries, each cell is one of three possible integers.</p>

<p>&nbsp;</p>

<ul>
	<li>0 means the cell is empty, so you can pass through;</li>
	<li>1 means the cell contains a cherry, that you can pick up and pass through;</li>
	<li>-1 means the cell contains a thorn that blocks your way.</li>
</ul>

<p>&nbsp;</p>

<p>Your task is to collect maximum number of cherries possible by following the rules below:</p>

<p>&nbsp;</p>

<ul>
	<li>Starting at the position (0, 0) and reaching (N-1, N-1) by moving right or down through valid path cells (cells with value 0 or 1);</li>
	<li>After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;</li>
	<li>When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);</li>
	<li>If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.</li>
</ul>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
<b>Output:</b> 5
<b>Explanation:</b> 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li><code>grid</code> is an <code>N</code> by <code>N</code> 2D array, with <code>1 &lt;= N &lt;= 50</code>.</li>
	<li>Each <code>grid[i][j]</code> is an integer in the set <code>{-1, 0, 1}</code>.</li>
	<li>It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.</li>
	<li>
	<p>&nbsp;</p>
	</li>
</ul>


-----------


## Similar Problems

- [Medium] [Minimum Path Sum](minimum-path-sum)

- [Hard] [Dungeon Game](dungeon-game)




## Solution:

[TOC]

#### Approach #1: Greedy [Wrong Answer]

**Intuition**

Let's find the most cherries we can pick up with one path, pick them up, then find the most cherries we can pick up with a second path on the remaining field.

Though a counter example might be hard to think of, this approach fails to find the best answer to this case:
```python
11100
00101
10100
00100
00111
```

**Algorithm**

We can use dynamic programming to find the most number of cherries `dp[i][j]` that can be picked up from any location `(i, j)` to the bottom right corner.  This is a classic question very similar to [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/description/), refer to the link if you are not familiar with this type of question.

After, we can find an first path that maximizes the number of cherries taken by using our completed `dp` as an oracle for deciding where to move.  We'll choose the move that allows us to pick up more cherries (based on comparing `dp[i+1][j]` and `dp[i][j+1]`).

After taking the cherries from that path (and removing it from the grid), we'll take the cherries again.

<iframe src="https://leetcode.com/playground/UVn8oEww/shared" frameBorder="0" width="100%" height="500" name="UVn8oEww"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^2)$$, where $$N$$ is the length of `grid`.  Our dynamic programming consists of two for-loops of length `N`.

* Space Complexity: $$O(N^2)$$, the size of `dp`.

---
#### Approach #2: Dynamic Programming (Top Down) [Accepted]

**Intuition**

Instead of walking from end to beginning, let's reverse the second leg of the path, so we are only considering two paths from the beginning to the end.

Notice after `t` steps, each position `(r, c)` we could be, is on the line `r + c = t`.  So if we have two people at positions `(r1, c1)` and `(r2, c2)`, then `r2 = r1 + c1 - c2`.  That means the variables `r1, c1, c2` uniquely determine 2 people who have walked the same `r1 + c1` number of steps.  This sets us up for dynamic programming quite nicely.

**Algorithm**

Let `dp[r1][c1][c2]` be the most number of cherries obtained by two people starting at `(r1, c1)` and `(r2, c2)` and walking towards `(N-1, N-1)` picking up cherries, where `r2 = r1+c1-c2`.

If `grid[r1][c1]` and `grid[r2][c2]` are not thorns, then the value of `dp[r1][c1][c2]` is `(grid[r1][c1] + grid[r2][c2])`, plus the maximum of `dp[r1+1][c1][c2]`, `dp[r1][c1+1][c2]`, `dp[r1+1][c1][c2+1]`, `dp[r1][c1+1][c2+1]` as appropriate.  We should also be careful to not double count in case `(r1, c1) == (r2, c2)`.

Why did we say it was the maximum of `dp[r+1][c1][c2]` etc.?  It corresponds to the 4 possibilities for person 1 and 2 moving down and right:

* Person 1 down and person 2 down: `dp[r1+1][c1][c2]`;
* Person 1 right and person 2 down: `dp[r1][c1+1][c2]`;
* Person 1 down and person 2 right: `dp[r1+1][c1][c2+1]`;
* Person 1 right and person 2 right: `dp[r1][c1+1][c2+1]`;


<iframe src="https://leetcode.com/playground/BbN9rraL/shared" frameBorder="0" width="100%" height="500" name="BbN9rraL"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^3)$$, where $$N$$ is the length of `grid`.  Our dynamic programming has $$O(N^3)$$ states.

* Space Complexity: $$O(N^3)$$, the size of `memo`.

---
#### Approach #3: Dynamic Programming (Bottom Up) [Accepted]

**Intuition**

Like in *Approach #2*, we have the idea of dynamic programming.

Say `r1 + c1 = t` is the `t`-th layer.  Since our recursion only references the next layer, we only need to keep two layers in memory at a time.

**Algorithm**

At time `t`, let `dp[c1][c2]` be the most cherries that we can pick up for two people going from `(0, 0)` to `(r1, c1)` and `(0, 0)` to `(r2, c2)`, where `r1 = t-c1, r2 = t-c2`.  Our dynamic program proceeds similarly to *Approach #2*.

<iframe src="https://leetcode.com/playground/SAAR75Ui/shared" frameBorder="0" width="100%" height="500" name="SAAR75Ui"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^3)$$, where $$N$$ is the length of `grid`.  We have three for-loops of size $$O(N)$$.

* Space Complexity: $$O(N^2)$$, the sizes of `dp` and `dp2`.

---

Analysis written by: [@awice](https://leetcode.com/awice).  Solution 3 inspired by [@uwi](https://leetcode.com/contest/weekly-contest-61/ranking).
