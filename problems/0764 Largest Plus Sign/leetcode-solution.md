# 0764 - Largest Plus Sign

Difficulty  | Tags | Links | Solutions
----------- | ---- | ----- | -----
Medium | Dynamic Programming | [Leetcode](https://leetcode.com/problems/largest-plus-sign) | [solution](https://leetcode.com/problems/largest-plus-sign/solution/)


-----------

<p>
In a 2D <code>grid</code> from (0, 0) to (N-1, N-1), every cell contains a <code>1</code>, except those cells in the given list <code>mines</code> which are <code>0</code>.  What is the largest axis-aligned plus sign of <code>1</code>s contained in the grid?  Return the order of the plus sign.  If there is none, return 0.
</p><p>
An "<i>axis-aligned plus sign of <code>1</code>s</i> of order <b>k</b>" has some center <code>grid[x][y] = 1</code> along with 4 arms of length <code>k-1</code> going up, down, left, and right, and made of <code>1</code>s.  This is demonstrated in the diagrams below.  Note that there could be <code>0</code>s or <code>1</code>s beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1s.
</p><p>

<p><b>Examples of Axis-Aligned Plus Signs of Order k:</b><br /><pre>
Order 1:
000
0<b>1</b>0
000

Order 2:
00000
00<b>1</b>00
0<b>111</b>0
00<b>1</b>00
00000

Order 3:
0000000
000<b>1</b>000
000<b>1</b>000
0<b>11111</b>0
000<b>1</b>000
000<b>1</b>000
0000000
</pre></p>

<p><b>Example 1:</b><br /><pre>
<b>Input:</b> N = 5, mines = [[4, 2]]
<b>Output:</b> 2
<b>Explanation:</b>
11111
11111
1<b>1</b>111
<b>111</b>11
1<b>1</b>011
In the above grid, the largest plus sign can only be order 2.  One of them is marked in bold.
</pre></p>

<p><b>Example 2:</b><br /><pre>
<b>Input:</b> N = 2, mines = []
<b>Output:</b> 1
<b>Explanation:</b>
There is no plus sign of order 2, but there is of order 1.
</pre></p>

<p><b>Example 3:</b><br /><pre>
<b>Input:</b> N = 1, mines = [[0, 0]]
<b>Output:</b> 0
<b>Explanation:</b>
There is no plus sign, so return 0.
</pre></p>

<p><b>Note:</b><br><ol>
<li><code>N</code> will be an integer in the range <code>[1, 500]</code>.</li>
<li><code>mines</code> will have length at most <code>5000</code>.</li>
<li><code>mines[i]</code> will be length 2 and consist of integers in the range <code>[0, N-1]</code>.</li>
<li><i>(Additionally, programs submitted in C, C++, or C# will be judged with a slightly smaller time limit.)</i></li>
</ol></p>

-----------


## Similar Problems

- [Medium] [Maximal Square](maximal-square)




## Solution:

[TOC]

#### Approach #1: Brute Force [Time Limit Exceeded]

**Intuition and Algorithm**

For each possible center, find the largest plus sign that could be placed by repeatedly expanding it.
We expect this algorithm to be $$O(N^3)$$, and so take roughly $$500^3 = (1.25) * 10^8$$ operations.  This is a little bit too big for us to expect it to run in time.

<iframe src="https://leetcode.com/playground/pVcrm4PA/shared" frameBorder="0" width="100%" height="412" name="pVcrm4PA"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^3)$$, as we perform two outer loops ($$O(N^2)$$), plus the inner loop involving `k` is $$O(N)$$.

* Space Complexity: $$O(\text{mines.length})$$.

---

#### Approach #2: Dynamic Programming [Accepted]

**Intuition**

How can we improve our bruteforce?  One way is to try to speed up the inner loop involving `k`, the order of the candidate plus sign.
If we knew the longest possible arm length $$L_u, L_l, L_d, L_r$$ in each direction from a center, we could know the order $$\min(L_u, L_l, L_d, L_r)$$ of a plus sign at that center.  We could find these lengths separately using dynamic programming.

**Algorithm**

For each (cardinal) direction, and for each coordinate `(r, c)` let's compute the `count` of that coordinate: the longest line of `'1'`s starting from `(r, c)` and going in that direction.
With dynamic programming, it is either 0 if `grid[r][c]` is zero, else it is `1` plus the count of the coordinate in the same direction.
For example, if the direction is left and we have a row like `01110110`, the corresponding count values are `01230120`, and the integers are either 1 more than their successor, or 0.
For each square, we want `dp[r][c]` to end up being the minimum of the 4 possible counts.  At the end, we take the maximum value in `dp`.

<iframe src="https://leetcode.com/playground/JxbvtwM9/shared" frameBorder="0" width="100%" height="500" name="JxbvtwM9"></iframe>

**Complexity Analysis**

* Time Complexity: $$O(N^2)$$, as the work we do under two nested for loops is $$O(1)$$.

* Space Complexity: $$O(N^2)$$, the size of `dp`.

---
Analysis written by: [@awice](https://leetcode.com/awice).
